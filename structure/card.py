import mysql as sql
import math
import structure.store as store
import json

order_way = {"id":"sc.ID", "price":"sc.Price", "quantity":"sc.Quantity"}

# Store Card
def storecardOutputFormat(output:list):
    require = ["storeCardId","name","actaulCardID","price","quantity","storeId","storeName"]
    res = {}
    for (k,v) in zip(require, output):
        res[k] = v
    return res

# 搜尋所有商品
def searchStoreCard(param:str, catagory:str, page:int, pageLimit:int, orderWay:str, ascending:bool):
    
    conditions= f'''StoreCard sc 
            Join Store s ON s.ID = sc.Store_ID
            Join ActualCard a ON a.ID = sc.ACCard_ID
            where sc.ACCard_ID IN 
            (Select ID from ActualCard
            where Name like "%{param}%" and Catagory like "%{catagory}%") '''
    
    total_row = sql.countTable(conditions)
    
    if total_row == 0:
        return "Not Found"
            
    cmd=f'''Select sc.ID, a.Name, a.ID, 
            sc.Price, sc.Quantity, sc.Store_ID,
            s.Name from '''         
    cmd += conditions    
    cmd += f" Order By {order_way[orderWay]} {'ASC' if ascending else 'DESC'}"
    cmd += f" Limit {(page-1)*pageLimit},{pageLimit}"
        
    result = [storecardOutputFormat(r) for r in sql.command(cmd)]
        
    total_page = math.ceil(total_row / pageLimit) 
    
    return {"totalPage":total_page, "items":result}

# 取得商品
def GetStoreCard(cardId:int):
    if sql.countTable(f"StoreCard where ID = {cardId}") == 0:
        return "Card not found"
    cmd = f'''Select sc.ID, a.Name, a.ID, 
            sc.Price, sc.Quantity, sc.Store_ID,
            s.Name,
            s.Description
            from StoreCard sc 
            Join Store s ON s.ID = sc.Store_ID
            Join ActualCard a ON a.ID = sc.ACCard_ID
            where s.ID = {cardId}'''
    result = sql.command(cmd)[0]
    return storecardOutputFormat(result)

# 查看商店的所有商品
def lookCardInStore(storeId:int, page:int, pageLimit:int, orderWay:str, ascending:bool):
    if sql.countTable(f"Store where ID = {storeId}") == 0:
        return "Store not found"
        
    cmd = f'''Select sc.ID, a.Name, a.ID,
            sc.Price, sc.Quantity from '''
                
    conditions = f'''StoreCard sc
            inner Join ActualCard a ON sc.ACCard_ID = a.ID
            inner Join Store s ON sc.Store_ID = s.ID
            where sc.Store_ID in
            (select ID from Store
            where ID = {storeId})
            '''
    
    cmd+=conditions
     
    cmd += f" Order By {order_way[orderWay]} {'ASC' if ascending else 'DESC'}"
    cmd += f" Limit {(page - 1)*pageLimit},{pageLimit}"
    
    result = [storecardOutputFormat(r) for r in sql.command(cmd)]
    total_row=sql.countTable(conditions)
    
    total_page = math.ceil(total_row / pageLimit)
    return {"totalPage":total_page, "items":result}

# 增加 StoreCard 到 Store
def AddStoreCard(data:dict):
    if sql.countTable(f"Store where ID = {data['storeId']}") == 0:
        return "Store not found"
    id = sql.getMaxId("StoreCard") + 1
    StoreCard_arg = [id,data["price"],data['status'],data['quantity'],data['ACCard_ID'],data['storeId']]
    sql.command(sql.insert("StoreCard",StoreCard_arg))
    store.updateStoreTime(getStore(id))
    return id

# 更新 StoreCard
def updateStoreCard(data:dict):
    if sql.countTable(f"StoreCard where ID = {data['cardId']}") == 0:
        return "Card not found"
    if sql.command(f"select store_id from StoreCard where ID =  {data['cardId']}")[0][0] != data['userId']:
        return "no access"
    store.updateStoreTime(getStore(data['cardId']))
    condition = [f"Price = {data['price']}"] if data.get('price') != None else []
    condition += [f"Status = '{data['status']}'"] if data.get('status') != None else []
    condition += [f"Quantity = {data['quantity']}"] if data.get('quantity') != None else []
    sql.command(f"update StoreCard set {','.join(condition)} where ID = {data['cardId']}")
    return "updated"

# 下架 StoreCard
def removeStoreCard(data:dict):
    if sql.countTable(f"StoreCard where ID = {data['cardId']}") == 0:
        return "Card not found"
    if sql.command(f"select store_id from StoreCard where ID =  {data['cardId']}")[0][0] != data['userId']:
        return "no access"
    store.updateStoreTime(getStore(data['cardId']))
    sql.command(f"DELETE FROM Order_to_Card_Table WHERE cardId = {data['cardId']}")
    sql.command(f"DELETE FROM Card_to_Cart_TableID WHERE cardId = {data['cardId']}")
    sql.command(f"DELETE FROM StoreCard WHERE ID = {data['cardId']}")
    return "removed"

def getPrice(cardId:int):
    if sql.countTable(f"StoreCard where ID = {cardId}") == 0:
        return "Card not found"
    return sql.command(f"SELECT Price FROM StoreCard where ID = {cardId}")[0][0]

# get store from store card
def getStore(cardId:int):
    cmd = f"Select store_id from StoreCard where ID = {cardId}"
    return sql.command(cmd)
    
# Actual Card

def actualcardOutputFormat(output:list):
    require = ["cardID", "name", "catagory", "description"]
    res = {}
    for (k,v) in zip(require, output):
        res[k] = v
    return res

# 查詢 ActualCard
def GetActualCard(cardId:int):
    if sql.countTable(f"ActualCard where ID = {cardId}") == 0:
        return "Card not found"
    cmd = f'''select * from ActualCard where ID = {cardId}'''
    return actualcardOutputFormat(sql.command(cmd)[0])

# 增加 ActualCard
def AddActualCard(data:dict):
    id = sql.getMaxId("ActualCard") + 1
    ActualCard_arg = [id, data['name'],data['catagory'],data['description']]
    sql.command(sql.insert("ActualCard",ActualCard_arg))
    return "added"

# 更新 ActualCard
def updateActualCard(data:dict):
    if sql.countTable(f"ActualCard where ID = {data['cardId']}") == 0:
        return "Card not found"
    condition = [f"Name = '{data['name']}'"] if data.get('name') != None else []
    condition += [f"Catagory = '{data['catagory']}'"] if data.get('catagory') != None else []
    condition += [f"Description = '{data['description']}'"] if data.get('description') != None else []
    sql.command(f"update ActualCard set {','.join(condition)} where ID = {data['cardId']}")
    return "updated"

# remove Actual Card
def removeActualCard(data:dict):
    if sql.countTable(f"ActualCard where ID = {data['cardId']}") == 0:
        return "Card not found"
    sql.command(f"Delete from StoreCard where ACCard_ID = {data['cardId']}")
    sql.command(f"Delete from ActualCard where ID = {data['cardId']}")
    return "removed"

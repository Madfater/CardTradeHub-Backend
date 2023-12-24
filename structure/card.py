import mysql as sql
import math
import structure.store as store

# Store Card

# 取得 StoreCard
def searchStoreCard(param:str, page:int, pageLimit:int, orderWay:str, ascending:bool):
    cmd = f'''Select sc.ID, a.Name, a.Catagory, a.Description,
            sc.Price, sc.Status, sc.Quantity, sc.ACCard_ID,
            sc.Store_ID, s.Description
            from StoreCard sc 
            Join Store s ON s.ID = sc.Store_ID
            Join ActualCard a ON a.ID = sc.ACCard_ID
            where sc.ACCard_ID IN 
            (Select ID from ActualCard
            where Name like "%{param}%" or Description like "%{param}%")
            '''
    order_way = {"id":"sc.ID", "price":"sc.Price", "quantity":"sc.Quantity"}
    cmd += f" Order By {order_way[orderWay]} {'ASC' if ascending else 'DESC'}"
    cmd += f" Limit {(page-1)*pageLimit},{pageLimit}"
    result = sql.command(cmd)
    total = len(result)
    if total == 0:
        result = "no results"
    total_page = math.floor(total / pageLimit) + 1 if total > 0 else 0
    output = {"total_page":total_page, "items":result}
    return output

# 取得 StoreCard
def GetStoreCard(Card_ID:int):
    if sql.countTable(f"StoreCard where ID = {Card_ID}") == 0:
        return "Card not found"
    cmd = f'''Select a.Name, a.Catagory, a.Description,
            sc.Price, sc.Status, sc.Quantity, sc.ACCard_ID,
            sc.Store_ID, s.Description
            from StoreCard sc 
            Join Store s ON s.ID = sc.Store_ID
            Join ActualCard a ON a.ID = sc.ACCard_ID
            where s.ID = {Card_ID}'''
    result = sql.command(cmd)[0]
    return result

# 增加 StoreCard 到 Store
def AddStoreCard(data:dict):
    if sql.countTable(f"Store where ID = {data['store_id']}") == 0:
        return "Store not found"
    id = sql.getMaxId("StoreCard") + 1
    StoreCard_arg = [id,data["price"],data['status'],data['quantity'],data['accard_ID'],data['store_id']]
    sql.command(sql.insert("StoreCard",StoreCard_arg))
    store.updateStoreTime(getStore(id))
    return id

# 更新 StoreCard
def updateStoreCard(data:dict):
    if sql.countTable(f"StoreCard where ID = {data['card_id']}") == 0:
        return "Card not found"
    if sql.command(f"select Store_ID from StoreCard where ID =  {data['card_id']}")[0][0] != data['user_id']:
        return "no access"
    store.updateStoreTime(getStore(data['card_id']))
    condition = [f"Price = {data['price']}"] if data.get('price') != None else []
    condition += [f"Status = '{data['status']}'"] if data.get('status') != None else []
    condition += [f"Quantity = {data['quantity']}"] if data.get('quantity') != None else []
    sql.command(f"update StoreCard set {','.join(condition)} where ID = {data['card_id']}")
    return "updated"

# 下架 StoreCard
def removeStoreCard(data:dict):
    if sql.countTable(f"StoreCard where ID = {data['card_id']}") == 0:
        return "Card not found"
    if sql.command(f"select Store_ID from StoreCard where ID =  {data['card_id']}")[0][0] != data['user_id']:
        return "no access"
    store.updateStoreTime(getStore(data['card_id']))
    sql.command(f"DELETE FROM Order_to_Card_Table WHERE Card_ID = {data['card_id']}")
    sql.command(f"DELETE FROM Card_to_Cart_TableID WHERE Card_ID = {data['card_id']}")
    sql.command(f"DELETE FROM StoreCard WHERE ID = {data['card_id']}")
    return "removed"

def getPrice(Card_ID:int):
    if sql.countTable(f"StoreCard where ID = {Card_ID}") == 0:
        return "Card not found"
    return sql.command(f"SELECT Price FROM StoreCard where ID = {Card_ID}")[0][0]

# get store from store card
def getStore(Card_ID:int):
    cmd = f"Select Store_ID from StoreCard where ID = {Card_ID}"
    return sql.command(cmd)
    
# Actual Card

# 查詢 ActualCard
def GetActualCard(card_id:int):
    if sql.countTable(f"ActualCard where ID = {card_id}") == 0:
        return "Card not found"
    cmd = f'''select * from ActualCard where ID = {card_id}'''
    return sql.command(cmd)

# 增加 ActualCard
def AddActualCard(data:dict):
    id = sql.getMaxId("ActualCard") + 1
    ActualCard_arg = [id, data['name'],data['catagory'],data['description'],data['imgPath']]
    sql.command(sql.insert("ActualCard",ActualCard_arg))
    return "added"

# 更新 ActualCard
def updateActualCard(data:dict):
    if sql.countTable(f"ActualCard where ID = {data['card_id']}") == 0:
        return "Card not found"
    condition = [f"Name = '{data['name']}'"] if data.get('name') != None else []
    condition += [f"Catagory = '{data['catagory']}'"] if data.get('catagory') != None else []
    condition += [f"Description = '{data['description']}'"] if data.get('description') != None else []
    condition += [f"imgPath = '{data['imgPath']}'"] if data.get('imgPath') != None else []
    sql.command(f"update ActualCard set {','.join(condition)} where ID = {data['card_id']}")
    return "updated"

# remove Actual Card
def removeActualCard(card_id:int):
    if sql.countTable(f"ActualCard where ID = {card_id}") == 0:
        return "Card not found"
    sql.command(f"Delete from StoreCard where ACCard_ID = {card_id}")
    sql.command(f"Delete from ActualCard where ID = {card_id}")
    return "removed"
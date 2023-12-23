import mysql as sql
import math
# Store Card

# 取得 StoreCard
def searchCard(data:dict):
    cmd = f'''Select sc.ID, sc.Price, sc.Status, sc.Quantity, sc.ACCard_ID,
            sc.Store_ID, s.Description, s.ModiefiedDate
            from StoreCard sc Join Store s ON s.ID = sc.Store_ID
            where sc.ACCard_ID IN 
            (Select ID from ActualCard
            where Name like "%{data['param']}%" or Description like "%{data['param']}%")
            '''
    order_way = {"id":"sc.ID", "price":"sc.Price", "quantity":"sc.Quantity"}
    cmd += f" Order By {order_way[data['orderWay']]} {'ASC' if data['ascending'] else 'DESC'}"
    cmd += f" Limit {(data['page']-1)*data['pageLimit']},{data['pageLimit']}"
    result = sql.command(cmd)
    total = len(result)
    total_page = math.floor(total / data['pageLimit']) + 1
    output = {"total_page":total_page, "items":result}
    return output

# 增加 StoreCard 到 Store
def AddCard(data:dict):
    id = sql.getMaxId("StoreCard") + 1
    StoreCard_arg = [id,data["price"],data['status'],data['quantity'],data['ACCard_ID'],data['Store_ID']]
    sql.command(sql.insert("StoreCard",StoreCard_arg))
    return "added"

# 更新 StoreCard
def updateCard(data:dict):
    if sql.countTable(f"StoreCard where ID = {data['Card_ID']}") == 0:
        return "Store ID not exist"
    condition = [f"Price = {data['price']}"] if data.get('price') != None else []
    condition += [f"Status = '{data['status']}'"] if data.get('status') != None else []
    condition += [f"Quantity = {data['Quantity']}"] if data.get('Quantity') != None else []
    sql.command(f"update StoreCard set {','.join(condition)} where ID = {data['Card_ID']}")
    return "updated"

# 下架 StoreCard
def removeCard(data:dict):
    if sql.countTable(f"StoreCard where ID = {data['Card_ID']}") == 0:
        return "Card ID not exist"
    if sql.command(f"select Store_ID from StoreCard where ID =  {data['Card_ID']}")[0][0] != data['User_ID']:
        return "no access"
    sql.command(f"DELETE FROM Order_to_Card_Table WHERE Card_ID = {data['Card_ID']}")
    sql.command(f"DELETE FROM Card_to_Cart_TableID WHERE Card_ID = {data['Card_ID']}")
    sql.command(f"DELETE FROM StoreCard WHERE ID = {data['Card_ID']}")
    return "removed"

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
def updateActualCard(card_id:int, data:dict):
    if sql.countTable(f"ActualCard where ID = {card_id}") == 0:
        return "Card not found"
    condition = [f"Name = '{data['name']}'"] if data.get('name') != None else []
    condition += [f"Catagory = '{data['catagory']}'"] if data.get('catagory') != None else []
    condition += [f"Description = '{data['description']}'"] if data.get('description') != None else []
    condition += [f"imgPath = '{data['imgPath']}'"] if data.get('imgPath') != None else []
    sql.command(f"update ActualCard set {','.join(condition)} where ID = {card_id}")
    return "updated"

# remove Actual Card
def removeActualCard(card_id:int):
    if sql.countTable(f"ActualCard where ID = {card_id}") == 0:
        return "Card not found"
    sql.command(f"Delete from StoreCard where ACCard_ID = {card_id}")
    sql.command(f"Delete from ActualCard where ID = {card_id}")
    return "removed"
import mysql as sql

# Store Card

# 取得 storecard
def searchCard(data:dict):
    cmd = f'''Select * from storeCard sc 
    where sc.ACCard_ID IN 
        (select Card_ID 
        from ActualCard where 
        Name like "%{data['param']}%" or Description like "%{data['param']}%"
        )
        Limit {(data['page']-1)*data['pageLimit']},{data['pageLimit']}
    '''
    return sql.command(cmd)

# 增加 storeCard
def AddCard(data:dict):
    id = sql.countTable("StoreCard") + 1
    storeCard_arg = [id,data["price"],data['status'],data['quantity'],data['ACCard_ID'],data['Store_ID']]
    sql.command(sql.insert("StoreCard",storeCard_arg))
    return "added"

# 更新 storeCard
def updateCard(data:dict):
    if sql.countTable(f"storeCard where Card_ID = {data['Card_ID']}") == 0:
        return "store Card_ID not exist"
    condition = [f"price = {data['price']}"] if data.get('price') != None else []
    condition += [f"status = '{data['status']}'"] if data.get('status') != None else []
    condition += [f"Quantity = {data['Quantity']}"] if data.get('Quantity') != None else []
    sql.command(f"update storeCard set {','.join(condition)} where Card_ID = {data['Card_ID']}")
    return "updated"



# Actual Card

# 查詢 ActualCard
def GetActualCard(data:dict):
    cmd = f'''select * from ActualCard where Card_ID = {data['Card_ID']}'''
    return sql.command(cmd)

# 增加 ActualCard
def AddActualCard(data:dict):
    id = sql.countTable("ActualCard") + 1
    ActualCard_arg = [id, data['name'],data['catagory'],data['description'],data['imgPath']]
    sql.command(sql.insert("ActualCard",ActualCard_arg))
    return "added"

# 更新 ActualCard
def updateActualCard(data:dict):
    if sql.countTable(f"ActualCard where Card_ID = {data['Card_ID']}") == 0:
        return "ActualCard Card_ID not exist"
    condition = [f"name = '{data['name']}'"] if data.get('name') != None else []
    condition += [f"catagory = '{data['catagory']}'"] if data.get('catagory') != None else []
    condition += [f"description = '{data['description']}'"] if data.get('description') != None else []
    condition += [f"imgPath = '{data['imgPath']}'"] if data.get('imgPath') != None else []
    sql.command(f"update ActualCard set {','.join(condition)} where Card_ID = {data['Card_ID']}")
    return "updated"
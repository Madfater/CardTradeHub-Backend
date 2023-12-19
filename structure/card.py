import mysql as sql
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
    if sql.command(f"select * from storeCard where Card_ID = {data['Card_ID']}"):
        return "store Card_ID not exist"
    condition = [f"price = {data['price']}"] if data.get('price') != None else []
    condition += [f"status = '{data['status']}'"] if data.get('status') != None else []
    condition += [f"Quantity = {data['Quantity']}"] if data.get('Quantity') != None else []
    sql.command(f"update storeCard set {','.join(condition)} where Card_ID = {data['Card_ID']}")
    return "updated"

# 取得 ActualCard
def GetActualCard(data:dict):
    cmd = f"select * from ActualCard where Card_ID = {data['Card_ID']}"
    return sql.command(cmd)

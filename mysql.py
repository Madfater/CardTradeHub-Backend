import pymysql
from datetime import datetime
import asyncio

# 資料輸入順序
User_order = ["Email","User_Name","Password"]

# 資料庫參數設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "1236987450", # 記得更改密碼
    "db": "testdb",
    "charset": "utf8"
}
# insert dst:table名稱 
def insert(dst:str, args:list):
    return f"INSERT INTO {dst} VALUES{tuple(args)}"

# 取得table內資料數
def countTable(table:str):
    return command(f"Select Count(*) From {table}")[0][0]

# 檢查user有無註冊過 用email檢查
def checkRegistered(email:str):
    return command(f"Select Count(*) From user where email = '{email}'")[0][0] != 0

# 註冊user
def registerUser(data:dict):
    if checkRegistered(data['email']):
        return "User already exist"
    id = countTable("user") + 1
    user_arg = [id]+[data[k] for k in User_order]+[0]+[id]*3
    store_arg = [id,"empty",str(datetime.today().date())]
    order_arg = [id,"empty",0]
    shopping_cart_arg = [id,0]
    command(insert("store",store_arg))
    command(insert("Order_list",order_arg))
    command(insert("shopping_cart",shopping_cart_arg))
    command(insert("user",user_arg))
    return "register success"

# 登陸user
def loginUser(data):
    if not checkRegistered(data['email']):
        return "this email isn\'t register yet"
    cmd = "Select password from user where email = "+ f"'{data['email']}'"
    acuratePassword = command(cmd)[0][0]
    return "login success" if data['password'] == acuratePassword else "login failed"

# 查購物車
def GetCart(data:dict):
    cmd = f"Select * from Shopping_Cart where Cart_ID = {data['User_ID']}"
    cmd += f" Limit {(data['page']-1)*data['pageLimit']},{data['pageLimit']}"
    return command(cmd)

# 查商店
def GetStore(data:dict):
    cmd = f"Select * from Store where Store_ID = {data['User_ID']}"
    cmd += f" Limit {(data['page']-1)*data['pageLimit']},{data['pageLimit']}"
    return command(cmd)

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
    return command(cmd)

# 增加 storeCard
def AddCard(data:dict):
    id = countTable("StoreCard") + 1
    storeCard_arg = [id,data["price"],data['status'],data['quantity'],data['ACCard_ID']]
    command(insert("StoreCard",store_arg))
    command(insert("Card_to_Store_Table",[countTable("Card_to_Store_Table")+1, data["Store_ID"], data["Card_ID"]]))
    return "added"

# 更新 storeCard
def updateCard(data:dict):
    if command(f"select * from storeCard where Card_ID = {data['Card_ID']}"):
        return "store Card_ID not exist"
    condition = [f"price = {data['price']}"] if data.get('price') != None else []
    condition += [f"status = '{data['status']}'"] if data.get('status') != None else []
    condition += [f"Quantity = {data['Quantity']}"] if data.get('Quantity') != None else []
    command(f"update storeCard set {','.join(condition)} where Card_ID = {data['Card_ID']}")
    return "updated"

# 取得 ActualCard
def GetActualCard(data:dict):
    cmd = f"select * from ActualCard where Card_ID = {data['Card_ID']}"
    return command(cmd)

# 增加評論
def AddComment(data:dict):
    id = countTable("comment") + 1
    comment_arg = [id,data['score'],data['context'],data['store_id'],data['user_id']]
    result = command(insert("comment",comment_arg))
    return "added" if not result else "add failed"
    
# 執行操作
def command(waitting_command:str):
    try:
        conn = pymysql.connect(**db_settings)
        with conn.cursor() as cursor:
            cursor.execute(waitting_command) # 執行SQL程式碼
            result = cursor.fetchall()
            conn.commit()
            return result # 輸出
    except Exception as ex:
        print('execute:',ex)
        return False
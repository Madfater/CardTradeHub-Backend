import mysql as sql
from datetime import datetime

# 資料輸入順序
User_order = ["email","username","password"]

# 檢查user有無註冊過 用email檢查
def checkRegistered(email:str):
    return sql.command(f"Select Count(*) From user where email = '{email}'")[0][0] != 0

# 註冊user
def registerUser(data:dict):
    if checkRegistered(data['email']):
        return "User already exist"
    id = sql.countTable("user") + 1
    user_arg = [id]+[data[k] for k in User_order]+[0]+[id]*3
    store_arg = [id,"empty",str(datetime.today().date())]
    order_arg = [id,"empty",0]
    shopping_cart_arg = [id,0]
    sql.command(sql.insert("store",store_arg))
    sql.command(sql.insert("Order_list",order_arg))
    sql.command(sql.insert("shopping_cart",shopping_cart_arg))
    sql.command(sql.insert("user",user_arg))
    return "register success"

# 登陸user
def loginUser(data):
    if not checkRegistered(data['email']):
        return "this email isn\'t register yet"
    cmd = "Select password from user where email = "+ f"'{data['email']}'"
    acuratePassword = sql.command(cmd)[0][0]
    return "login success" if data['password'] == acuratePassword else "login failed"

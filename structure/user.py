import mysql as sql
from datetime import datetime

# 資料輸入順序
User_order = ["email","username","password"]

# 註冊user
def registerUser(data:dict):
    if sql.countTable(f"user where email = '{data['email']}'") != 0:
        return "User already exist"
    id = sql.countTable("user") + 1
    user_arg = [id]+[data[k] for k in User_order]+[0]+[id]*2
    store_arg = [id,"empty",str(datetime.today().date())]
    order_arg = [id,"empty",0,id]
    shopping_cart_arg = [id,0]
    sql.command(sql.insert("store",store_arg))
    sql.command(sql.insert("shopping_cart",shopping_cart_arg))
    sql.command(sql.insert("user",user_arg))
    sql.command(sql.insert("Order_list",order_arg))
    return "register success"

# 登陸user
def loginUser(data):
    if sql.countTable(f"user where email = '{data['email']}'") == 0:
        return "this email isn't register yet"
    cmd = "Select password from user where email = "+ f"'{data['email']}'"
    acuratePassword = sql.command(cmd)[0][0]
    return "login success" if data['password'] == acuratePassword else "login failed"

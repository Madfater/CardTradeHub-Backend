import mysql as sql
from datetime import datetime

# 資料輸入順序
User_order = ["email","username","password"]

# 註冊User
def registerUser(data:dict):
    if sql.countTable(f"User where Email = '{data['email']}'") != 0:
        return "User already exist"
    id = sql.getMaxId("User") + 1
    User_arg = [id]+[data[k] for k in User_order]+[0]+[id]*2
    store_arg = [id,"empty",str(datetime.today().date())]
    order_arg = [id,"empty",0,id]
    shopping_cart_arg = [id,0]
    sql.command(sql.insert("Store",store_arg))
    sql.command(sql.insert("Shopping_Cart",shopping_cart_arg))
    sql.command(sql.insert("User",User_arg))
    sql.command(sql.insert("Order_List",order_arg))
    return "register success"

# 登陸User
def loginUser(data):
    if sql.countTable(f"User where Email = '{data['email']}'") == 0:
        return "this email isn't register yet"
    cmd = "Select Password from User where Email = "+ f"'{data['email']}'"
    acuratePassword = sql.command(cmd)[0][0]
    return "login success" if data['password'] == acuratePassword else "login failed"

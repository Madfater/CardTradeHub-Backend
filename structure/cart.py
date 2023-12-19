import mysql as sql
# 查購物車
def GetCart(data:dict):
    cmd = f"Select * from Shopping_Cart where Cart_ID = {data['User_ID']}"
    cmd += f" Limit {(data['page']-1)*data['pageLimit']},{data['pageLimit']}"
    return sql.command(cmd)
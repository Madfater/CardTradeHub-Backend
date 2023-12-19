import mysql
# 取得order
def GetOrder(data:dict):
    cmd = f"SELECT * FROM Order_List where order_id = {data['order_id']}"

import mysql as sql
import math
from datetime import datetime
# 查商店的 Store Card
def lookStore(Store_ID:int, page:int, pageLimit:int, orderWay:str, ascending:bool):
    if sql.countTable(f"Store where ID = {Store_ID}") == 0:
        return "Store not found"
    cmd = f'''select sc.ID, sc.Price, sc.Status, sc.Quantity, sc.Store_ID, 
                ac.Name, ac.Catagory, ac.Description,
                from StoreCard sc
                Join ActualCard ac ON sc.ACCard_ID = ac.ID
                where sc.Store_ID in
                (select ID from Store
                where ID = {Store_ID}
            )'''
    order_way = {"id":"sc.ID", "price":"sc.Price", "quantity":"sc.Quantity"}
    cmd += f" Order By {order_way[orderWay]} {'ASC' if ascending else 'DESC'}"
    cmd += f" Limit {(page - 1)*pageLimit},{pageLimit}"
    result = sql.command(cmd)
    total = len(result)
    total_page = math.floor(total / pageLimit) + 1
    output = {"total_page":total_page, "items":result}
    return output

# update store ModiefiedDate
def updateStoreTime(Store_ID:int):
    cmd = f"update Store set ModiefiedDate = '{str(datetime.today().date())}' where Store.ID = {Store_ID}"
    sql.command(cmd)
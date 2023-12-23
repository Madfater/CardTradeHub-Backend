import mysql as sql
import math
# 查商店的 Store Card
def lookStore(User_ID:int, data:dict = {'orderWay':"id", 'ascending':True}, page:int = 1, page_limit:int = 30):
    cmd = f'''select sc.ID, sc.Price, sc.Status, sc.Quantity, sc.Store_ID, 
                ac.Name, ac.Catagory, ac.Description, ac.imgPath
                from StoreCard sc
                Join ActualCard ac ON sc.ACCard_ID = ac.ID
                where sc.Store_ID in
                (select ID from Store
                where ID = 1
            )'''
    order_way = {"id":"sc.ID", "price":"sc.Price", "quantity":"sc.Quantity"}
    cmd += f" Order By {order_way[data['orderWay']]} {'ASC' if data['ascending'] else 'DESC'}"
    cmd += f" Limit {(page - 1)*page_limit},{page_limit}"
    result = sql.command(cmd)
    total = len(result)
    total_page = math.floor(total / page_limit) + 1
    output = {"total_page":total_page, "items":result}
    return output
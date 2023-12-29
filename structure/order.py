import mysql as sql
import structure.card as card
import math
def OrderOutputFormat(output:list):
    require = ["storeCardID","storeCardPrice","orderQuantity","actualCardID","storeID","isComment","actualCardName","actualCardCatagory","storeName"]
    res = {}
    for (k,v) in zip(require, output):
        res[k] = v
    return res

# 取得order
def lookOrder(Order_id: int, page: int, pageLimit:int):
    
    cmd = f'''select sc.ID, sc.Price, oc.Quantity,sc.ACCard_ID,sc.Store_ID,o.IsComment,ac.Name,ac.Catagory,s.Name,o.ID from '''
    
    conditions =f'''StoreCard sc
            inner join Order_to_Card_Table oc ON oc.Card_ID = sc.ID
            inner join Order_List o ON o.ID = oc.Order_ID
            inner Join ActualCard ac ON ac.ID = sc.ACCard_ID
            inner Join Store s ON s.ID = sc.Store_ID
            where o.User_ID = {Order_id}'''
            
    cmd += conditions
    cmd += f" Limit {(page-1)*pageLimit},{pageLimit}"
    result = sql.command(cmd)
    items = {}
    for r in result:
        if items.get(r[-1]) == None:
            items[r[-1]] = [OrderOutputFormat(r)]
        else:
            items[r[-1]] += [OrderOutputFormat(r)]
            
    total = sql.countTable(conditions)
    total_page = math.ceil(total / pageLimit) 
    output = {"totalPage" : total_page, "items" : items}
    return output

# add order
def addOrder(data:dict):
    if sql.countTable(f"User where ID = {data['userId']}") == 0:
        return "User not found"
    order_id = sql.getMaxId("Order_List") + 1
    order_list_args = [order_id, data['address'], 0, int(data['userId']),False]
    
    sql.command(sql.insert(f"Order_List", order_list_args))
    total_price = 0

    for item in data["items"]:
        total_price += card.getPrice(item["cardId"]) * item["quantity"]
        sql.command(sql.insert("Order_to_Card_Table",[sql.getMaxId("Order_to_Card_Table")+1, item["quantity"], order_id, item["cardId"]]))
    sql.command(f"update Order_List set Total_Price = {total_price} where ID = {order_id}")
    return order_id

# remove order
def removeOrder(data:dict):
    if sql.countTable(f"Order_List where ID = {data['order_id']}") == 0:
        return "Order not found"
    sql.command(f"DELETE FROM Order_to_Card_Table WHERE Order_ID = {data['order_id']}")
    sql.command(f"DELETE FROM Order_List WHERE ID = {data['order_id']}")
    return "removed"

# update card from shopping cart
def updateOrder(data:dict):
    if sql.countTable(f"Order_List where ID = {data['Id']}") == 0:
        return "Order not found"
        
    sql.command(f'''UPDATE Order_List
                    SET IsComment = true
                    WHERE ID = {data['Id']}''')
    return "updated"
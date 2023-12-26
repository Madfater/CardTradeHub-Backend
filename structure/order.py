import mysql as sql
import structure.card as card
import math
def OrderOutputFormat(output:list):
    require = ["storeCardID","storeCardPrice","orderQuantity","actualCardID"]
    res = {}
    for (k,v) in zip(require, output):
        res[k] = v
    return res

# 取得order
def lookOrder(Order_id: int, page: int, pageLimit:int):
    if sql.countTable(f"Order_List where ID = {Order_id}") == 0:
        return "Order not found"
    cmd = f'''select sc.ID, sc.Price, oc.Quantity,sc.ACCard_ID,sc.Store_ID
            from StoreCard sc
            inner join Order_to_Card_Table oc ON oc.Card_ID = sc.ID
            inner join Order_List o ON o.ID = oc.Order_ID
            where o.ID = {Order_id}
            '''
    cmd += f" Limit {(page-1)*pageLimit},{pageLimit}"
    result = sql.command(cmd)
    items = {}
    for r in result:
        if items.get(r[-1]) == None:
            items[r[-1]] = [OrderOutputFormat(r[:-1])]
        else:
            items[r[-1]] += [OrderOutputFormat(r[:-1])]
    total = len(result)
    totalpage = math.floor(total / pageLimit) + 1
    output = {"totalpage" : totalpage, "items" : items}
    return output

# add order
def addOrder(data:dict):
    if sql.countTable(f"User where ID = {data['userId']}") == 0:
        return "User not found"
    order_id = sql.getMaxId("Order_List") + 1
    order_list_args = [order_id, data['address'], 0, int(data['userId'])]
    sql.command(sql.insert(f"Order_List", order_list_args))
    total_price = 0
    for (cardId,quantity) in data["items"].items():
        total_price += card.getPrice(cardId) * quantity
        sql.command(sql.insert("Order_to_Card_Table",[sql.getMaxId("Order_to_Card_Table")+1, quantity, order_id, cardId]))
    sql.command(f"update Order_List set Total_Price = {total_price} where ID = {order_id}")
    return order_id

# remove order
def removeOrder(data:dict):
    if sql.countTable(f"Order_List where ID = {data['order_id']}") == 0:
        return "Order not found"
    sql.command(f"DELETE FROM Order_to_Card_Table WHERE Order_ID = {data['order_id']}")
    sql.command(f"DELETE FROM Order_List WHERE ID = {data['order_id']}")
    return "removed"
import mysql as sql
import math

def shoppingcartOutputFormat(output:list):
    require = ["storeCardId","storeCardPrice","storeCardStatus","storeCardQuantity","cardName","cardCategory", "cardDescription"]
    res = {}
    for (k,v) in zip(require, output):
        res[k] = v
    return res

# 查購物車
def lookCart(userId:int,page:int = 1, pageLimit:int = 30):
    if sql.countTable(f"User where ID = {userId}") == 0:
        return "User not found"
        
    cmd = f'''select sc.ID, sc.Price, sc.Status, sc.Quantity,
        ac.Name, ac.Catagory,
        ac.Description, sc.Store_ID
        from '''
        
    conditions = f'''StoreCard sc
        inner join Card_to_Cart_Table cctable ON cctable.Card_ID = sc.ID
        inner join Shopping_Cart scart ON scart.ID = cctable.Cart_ID
        inner join ActualCard ac ON ac.ID = sc.ACCard_ID
        where scart.ID = {userId}'''
    
    cmd += conditions
    cmd += f" Limit {(page - 1)*pageLimit},{pageLimit}"
    
    result = sql.command(cmd)
    items = {}
    
    for r in result:
        if items.get(r[-1]) == None:
            items[r[-1]] = [shoppingcartOutputFormat(r[:-1])]
        else:
            items[r[-1]] += [shoppingcartOutputFormat(r[:-1])]
            
    total_row = sql.countTable(conditions)
    total_page = math.ceil(total_row / pageLimit)
    output = {"totalPage":total_page, "items":items}
    return output
    
# 加入Store card到 shopping cart
def addCard(data:dict):
    if sql.countTable(f"User where ID = {data['userId']}") == 0:
        return "User not found"
    if sql.countTable(f"StoreCard where ID = {data['cardId']}") == 0:
        return "Card not found"
    id = sql.getMaxId("Card_to_Cart_Table") + 1
    card_to_cart_arg = [id, data['quantity'], data['userId'], data['cardId']]
    sql.command(sql.insert("Card_to_Cart_Table",card_to_cart_arg))
    return "added"

# remove card from shopping cart
def removeCard(data:dict):
    if sql.countTable(f"User where ID = {data['userId']}") == 0:
        return "User not found"
    if sql.countTable(f"StoreCard where ID = {data['cardId']}") == 0:
        return "Card not found"
    if sql.countTable(f"Card_to_Cart_Table where cardId = {data['cardId']}") == 0:
        return "Card not in shopping cart"
    sql.command(f'''Delete From Card_to_Cart_Table 
                where cardId = {data['cardId']} 
                and Cart_ID = {data['userId']}''')
    return "removed"
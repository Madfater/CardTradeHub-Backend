import mysql as sql
import math
# 查購物車
def lookCart(User_ID:int,page:int = 1, pageLimit:int = 30):
    if sql.countTable(f"User where ID = {User_ID}") == 0:
        return "User not found"
    cmd = f'''select sc.ID,Price,sc.Status,sc.Quantity,sc.ACCard_ID,sc.Store_ID
    from StoreCard sc
    inner join Card_to_Cart_Table cctable ON cctable.Card_ID = sc.ID
    inner join Shopping_Cart scart ON scart.ID = cctable.Cart_ID
    where scart.ID = {User_ID}'''
    cmd += f" Limit {(page - 1)*pageLimit},{pageLimit}"
    result = sql.command(cmd)
    total = len(result)
    total_page = math.floor(total / pageLimit) + 1
    output = {"total_page":total_page, "items":result}
    return output
    
# 加入Store card到 shopping cart
def addCard(User_ID:int, Card_ID:int):
    if sql.countTable(f"User where ID = {User_ID}") == 0:
        return "User not found"
    if sql.countTable(f"StoreCard where ID = {Card_ID}") == 0:
        return "Card not found"
    id = sql.getMaxId("Card_to_Cart_Table") + 1
    card_to_cart_arg = [id, User_ID, Card_ID]
    sql.command(sql.insert("Card_to_Cart_Table",card_to_cart_arg))
    return "added"

# remove card from shopping cart
def removeCard(User_ID:int, Card_ID:int):
    if sql.countTable(f"User where ID = {User_ID}") == 0:
        return "User not found"
    if sql.countTable(f"StoreCard where ID = {Card_ID}") == 0:
        return "Card not found"
    if sql.countTable(f"Card_to_Cart_Table where Card_ID = {Card_ID}") == 0:
        return "Card not in shopping cart"
    sql.command(f'''Delete From Card_to_Cart_Table 
                where Card_ID = {Card_ID} 
                and Cart_ID = {User_ID}''')
    return "removed"
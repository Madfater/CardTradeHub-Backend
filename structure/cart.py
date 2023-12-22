import mysql as sql
# 查購物車
def GetCardInCart(data:dict):
    cmd = f'''select sc.ID,Price,sc.Status,sc.Quantity,sc.ACCard_ID,sc.Store_ID
    from StoreCard sc
    inner join Card_to_Cart_TableID cctable ON cctable.Card_ID = sc.ID
    inner join Shopping_Cart scart ON scart.ID = cctable.Cart_ID
    where scart.ID = {data['User_ID']}'''
    cmd += f" Limit {(data['page']-1)*data['pageLimit']},{data['pageLimit']}"
    return sql.command(cmd)

# 加入Store card到 shopping cart
def AddCardtoCart(data:dict):
    id = sql.getMaxId("Card_to_Cart_Table") + 1
    card_to_cart_arg = [id, data['User_ID'],data['Card_ID']]
    sql.command(sql.insert("Card_to_Cart_Table",card_to_cart_arg))
    return "added"

# remove card from shopping cart
def removeCardFromCart(data:dict):
    if sql.countTable(f"Card_to_Cart_Table where Card_ID = {data['Card_id']}") == 0:
        return "Card_ID not exists"
    sql.command(f"Delete From Card_to_Cart_Table where Card_ID = {data['Card_id']} and Cart_ID = {data['Cart_id']}")
    return "removed"
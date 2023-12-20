import mysql as sql
# 查購物車
def GetCart(data:dict):
    cmd = f'''select sc.Card_ID,Price,sc.Status,sc.Quantity,sc.ACCard_ID,sc.Store_ID
    from StoreCard sc
    inner join Card_to_Cart_TableID cctable ON cctable.Card_ID = sc.Card_ID
    inner join Shopping_Cart scart ON scart.Cart_ID = cctable.Cart_ID
    where scart.Cart_ID = {data['User_ID']}'''
    cmd += f" Limit {(data['page']-1)*data['pageLimit']},{data['pageLimit']}"
    return sql.command(cmd)

# 加入Store card到 shopping cart
def AddCart(data:dict):
    id = sql.countTable("Card_to_Cart_TableID") + 1
    card_to_cart_arg = [id, data['Cart_ID'],data['Card_id']]
    sql.command(sql.insert("Card_to_Cart_TableID",card_to_cart_arg))
    return "added"
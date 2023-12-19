import mysql as sql
# 取得order
def GetOrder(data:dict):
    cmd = f'''select sc.Card_ID,Price,sc.Status,sc.Quantity,sc.ACCard_ID,sc.Store_ID
    from StoreCard sc
    inner join Order_to_Card_Table oc ON oc.Card_ID = sc.Card_ID
    inner join Order_List o ON o.Order_ID = oc.Order_ID
    where o.Order_ID = {data['Order_id']}
    '''
    cmd += f" Limit {(data['page']-1)*data['pageLimit']},{data['pageLimit']}"
    return sql.command(cmd)
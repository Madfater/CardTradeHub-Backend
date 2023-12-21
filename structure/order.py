import mysql as sql
# 取得order
def GetOrder(data:dict):
    cmd = f'''select sc.ID,Price,sc.Status,sc.Quantity,sc.ACCard_ID,sc.Store_ID
    from StoreCard sc
    inner join Order_to_Card_Table oc ON oc.Card_ID = sc.ID
    inner join Order_List o ON o.ID = oc.Order_ID
    where o.ID = {data['Order_id']}
    '''
    cmd += f" Limit {(data['page']-1)*data['pageLimit']},{data['pageLimit']}"
    return sql.command(cmd)
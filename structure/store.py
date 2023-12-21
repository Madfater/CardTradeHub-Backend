import mysql as sql
# 查商店的 Store Card
def GetStore(data:dict):
    cmd = f'''select * from StoreCard 
    where StoreCard.Store_ID in 
	    (select ID from Store 
        where ID = {data['Store_ID']}
    )'''
    cmd += f" Limit {(data['page']-1)*data['pageLimit']},{data['pageLimit']}"
    return sql.command(cmd)
import mysql as sql
# 查商店的 store Card
def GetStore(data:dict):
    cmd = f'''select * from storeCard 
    where storeCard.store_id in 
	    (select Store_ID from store 
        where store_id = {data['Store_ID']}
    )'''
    cmd += f" Limit {(data['page']-1)*data['pageLimit']},{data['pageLimit']}"
    return sql.command(cmd)
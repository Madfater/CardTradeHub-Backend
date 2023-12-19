import mysql as sql
# 查商店
def GetStore(data:dict):
    cmd = f"Select * from Store where Store_ID = {data['Store_ID']}"
    cmd += f" Limit {(data['page']-1)*data['pageLimit']},{data['pageLimit']}"
    return sql.command(cmd)
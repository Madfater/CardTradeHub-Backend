import mysql as sql
import math
from datetime import datetime

def StoreOutputFormat(output:list):
    require = ["storeID","storeName","description"]
    res = {}
    for (k,v) in zip(require, output):
        res[k] = v
    return res

# 查 store
def GetStore(storeId:int):
    if sql.countTable(f"Store where ID = {storeId}") == 0:
        return "Store not found"
    cmd = f"Select ID, Name, Description from Store where ID = {storeId}"
    return StoreOutputFormat(sql.command(cmd)[0])

# store update
def updateStore(data:dict):
    if sql.countTable(f"Store where ID = {data['storeId']}") == 0:
        return "Store not found"
    cmd = "UPDATE Store SET"
    cmd += f" Name = {data['name']}" if data.get('name') is not None else ""
    cmd += f" Description = {data['description']}" if data.get('description') is not None else ""
    sql.command(cmd)
    updateStoreTime(data['storeId'])
    return "updated"

# update store ModiefiedDate
def updateStoreTime(storeId:int):
    cmd = f"update Store set ModiefiedDate = '{str(datetime.today().date())}' where Store.ID = {storeId}"
    sql.command(cmd)
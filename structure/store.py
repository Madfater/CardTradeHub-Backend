import mysql as sql
import math
from datetime import datetime

def StoreOutputFormat(output:list):
    require = ["storeID","storeName","description"]
    res = {}
    for (k,v) in zip(require, output):
        res[k] = v
    return res

# 取得 store 資訊
def GetStore(storeId:int):
    if sql.countTable(f"Store where ID = {storeId}") == 0:
        return "Store not found"
    cmd = f"Select ID, Name, Description from Store where ID = {storeId}"
    return StoreOutputFormat(sql.command(cmd)[0])

def SearchStore(param:str,page:int,pageLimit:int):
    
    conditions= f'''Store where Name like "%{param}%" '''
    
    total_row = sql.countTable(conditions)
    
    if total_row == 0:
        return "Not Found"
            
    cmd="Select * from "      
    cmd += conditions    
    cmd += f" Limit {(page-1)*pageLimit},{pageLimit}"
        
    result = [StoreOutputFormat(r) for r in sql.command(cmd)]
        
    total_page = math.ceil(total_row / pageLimit) 
    
    return {"totalPage":total_page, "items":result}

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
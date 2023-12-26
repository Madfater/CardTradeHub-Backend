import mysql as sql
import math
def CommentOutputFormat(output:list):
    require = ["commentID","score","context","userID"]
    res = {}
    for (k,v) in zip(require, output):
        res[k] = v
    return res

# 取評論
def lookComment(storeId:int,page:int = 1,pageLimit:int = 30):
    if sql.countTable(f"Store where ID = {storeId}") == 0:
        return "Store not found"
    
    cmd = f"SELECT ID, Score, Context, User_ID FROM "
    
    conditions = f"Comment WHERE Store_ID = {storeId}"
    
    cmd += conditions
    cmd += f" Limit {(page - 1)*pageLimit},{pageLimit}"
    
    result = [CommentOutputFormat(r) for r in sql.command(cmd)]
    total_row = sql.countTable(conditions)
    
    total_page = math.ceil(total_row / pageLimit)
    output = {"totalPage":total_page, "items":result}
    return output

# 增加評論
def AddComment(data:dict):
    if sql.countTable(f"Store where ID = {data['storeId']}") == 0:
        return "Store not found"
    if sql.countTable(f"User where ID = {data['userId']}") == 0:
        return "User not found"
    id = sql.getMaxId("Comment") + 1
    Comment_arg = [id,data['score'],data['context'], data['storeId'], data['userId']]
    sql.command(sql.insert("Comment",Comment_arg))
    return "added"

# update comment
def updateComment(data:dict):
    if sql.countTable(f"Comment where ID = {data['comment_id']}") == 0:
        return "Comment not found"
    condition = [f"Score = {data['score']}"] if data.get('score') != None else []
    condition += [f"Context = '{data['context']}'"] if data.get('context') != None else []
    sql.command(f"update Comment set {','.join(condition)} where ID = {data['comment_id']}")
    return "updated"

# delete comment
def removeComment(data:dict):
    if sql.countTable(f"Comment where ID = {data['comment_id']}") == 0:
        return "Comment not found"
    sql.command(f"DELETE FROM Comment where ID = {data['comment_id']}")
    return "removed"
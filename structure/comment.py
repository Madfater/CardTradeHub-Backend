import mysql as sql
import math
# 取評論
def lookComment(store_id:int,page:int = 1,pageLimit:int = 30):
    if sql.countTable(f"Store where ID = {store_id}") == 0:
        return "Store not found"
    cmd = f"SELECT ID, Score, Context, User_ID FROM Comment WHERE Store_ID = {store_id}"
    cmd += f" Limit {(page - 1)*pageLimit},{pageLimit}"
    result = sql.command(cmd)
    total = len(result)
    total_page = math.floor(total / pageLimit) + 1
    output = {"total_page":total_page, "items":result}
    return output

# 增加評論
def AddComment(data:dict):
    if sql.countTable(f"Store where ID = {data['store_id']}") == 0:
        return "Store not found"
    if sql.countTable(f"User where ID = {data['user_id']}") == 0:
        return "User not found"
    id = sql.getMaxId("Comment") + 1
    Comment_arg = [id,data['score'],data['context'], data['store_id'], data['user_id']]
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
def removeComment(comment_id:int):
    if sql.countTable(f"Comment where ID = {comment_id}") == 0:
        return "Comment not found"
    sql.command(f"DELETE FROM Comment where ID = {comment_id}")
    return "removed"
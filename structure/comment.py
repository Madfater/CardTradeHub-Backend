import mysql as sql
# 增加評論
def AddComment(data:dict):
    id = sql.getMaxId("Comment") + 1
    Comment_arg = [id,data['score'],data['context'],data['store_id'],data['user_id']]
    result = sql.command(sql.insert("Comment",Comment_arg))
    return "added" if not result else "add failed"

# update comment
def updateComment(data:dict):
    if sql.countTable(f"Comment where ID = {data['Comment_id']}") == 0:
        return "Comment not found"
    condition = [f"Score = {data['score']}"] if data.get('score') != None else []
    condition += [f"Context = '{data['context']}'"] if data.get('context') != None else []
    sql.command(f"update Comment set {','.join(condition)} where ID = {data['Comment_id']}")
    return "Comment updated"

# delete comment
def removeComment(data:dict):
    if sql.countTable(f"Comment where ID = {data['Comment_id']}") == 0:
        return "Comment not found"
    sql.command(f"DELETE FROM Comment where ID = {data['Comment_id']}")
    return "Comment deleted"
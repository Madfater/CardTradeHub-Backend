import mysql as sql
# 增加評論
def AddComment(data:dict):
    id = sql.getMaxId("Comment") + 1
    Comment_arg = [id,data['score'],data['context'],data['store_id'],data['user_id']]
    result = sql.command(sql.insert("Comment",Comment_arg))
    return "added" if not result else "add failed"
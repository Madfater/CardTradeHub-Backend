import mysql as sql
# 增加評論
def AddComment(data:dict):
    id = sql.countTable("comment") + 1
    comment_arg = [id,data['score'],data['context'],data['store_id'],data['user_id']]
    result = sql.command(sql.insert("comment",comment_arg))
    return "added" if not result else "add failed"
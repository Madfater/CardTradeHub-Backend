import pymysql

# 資料庫參數設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "", # 記得更改密碼
    "db": "testdb",
    "charset": "utf8"
}
# insert dst:table名稱 
def insert(dst:str, args:list):
    return f"INSERT INTO {dst} VALUES{tuple(args)}"

# 取得table內資料數
def countTable(table:str):
    return command(f"Select Count(*) From {table}")[0][0]

# 執行操作
def command(waitting_command:str):
    try:
        conn = pymysql.connect(**db_settings)
        with conn.cursor() as cursor:
            cursor.execute(waitting_command) # 執行SQL程式碼
            result = cursor.fetchall()
            conn.commit()
            return result # 輸出
    except Exception as ex:
        print("Exception:", ex)
        return ex
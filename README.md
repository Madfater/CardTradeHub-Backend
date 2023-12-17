# CardShop-Backend

## 測試POST 改後端資料庫成功

### HOW TO TEST

開MySQL 執行 [腳本](https://github.com/Madfater/CardShop/blob/backend_qq816/Backend/Sql_Init.txt)

Python套件記得裝

記得改MySQL密碼 [這裡](https://github.com/Madfater/CardShop/blob/backend_qq816/Backend/mysql.py)

執行[api.py](https://github.com/Madfater/CardShop/blob/backend_qq816/Backend/api.py)

POST 127.0.0.1:5000/api/user

測試用JSON檔


### request json format
login
```python
{
    "type": "login" ,
    "email": "123@gmail.com",
    "password": "passwd"
}
```
return "login success" or "login failed"


register
```python
{
    "type": "register",
    "password": "passwd",
    "username": "alan",
    "email": "123@gmail.com"
}
```
return "User already exist" or "register success"

GetCard
```python
{
    "type" : "GetCard", 
    "param" : "龍",
    "page" : 1,
    "pageLimit" : 40
}
```
return storeCard likes
```python
[
    [
        1,                  # CardID
        500,                # price
        "九成新狀態良好",    # status
        10,                 # quantity
        1                   # ACCard_ID
    ],
    [
        2,
        15,
        "舊卡新賣",
        20,
        2
    ]
]
```

GetActualCard
```python
{
    "type" : "GetActualCard", 
    "Card_ID" : 1           # ACCard_ID from storeCard
}
```
updateCard
```python
{
    "type" : "updateCard", 
    "Card_ID" : 1,    # storeCard ID
    "price" : 114514,
    "status" : "still new",
    "Quantity":999
}
```
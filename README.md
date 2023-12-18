# CardShop-Backend

## 測試POST 改後端資料庫成功

### HOW TO TEST

開MySQL 執行 [腳本](https://github.com/Madfater/CardShop/blob/backend_qq816/Backend/Sql_Init.txt)

Python套件記得裝

記得改MySQL密碼 [這裡](https://github.com/Madfater/CardShop/blob/backend_qq816/Backend/mysql.py)

執行[api.py](https://github.com/Madfater/CardShop/blob/backend_qq816/Backend/api.py)


測試用JSON檔


## request json format
### login 
```python
# /login , method = GET
{
    "email": "123@gmail.com",
    "password": "passwd"
}
```
return "login success" or "login failed"


### register
```python
# /register , method = POST
{
    "password": "passwd",
    "username": "alan",
    "email": "123@gmail.com"
}
```
return "User already exist" or "register success"

### GetCard
```python
# /get/storeCard/ , method = GET
{
    "param" : "一",         # 搜尋關鍵字
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

### GetActualCard
```python
# /get/actualCard/ , method = GET
{
    "Card_ID" : 1           # ACCard_ID from storeCard
}
```
return ActualCard likes
```python
[
    [
        1,                             # Card_ID
        "青眼白龍",                     # Name
        "怪獸卡",                       # Catagory
        "超猛飛龍毀滅一切",              # Description
        "https://imgur.com/a/2FFGPMs"   # imgPath
    ]
]
```

### AddComment
```python
# /comment , method = POST
{
    "score" : 5,
    "context" : "777",
    "store_id" : 2,
    "user_id":1
}

```
return "added" or "add failed"

### updateCard
```python
# /update , method = PUT
{
    "Card_ID" : 1,    # storeCard ID 
    "price" : 114514,
    "status" : "still new",
    "Quantity":999
    # 至少包含 price status Quantity其中一項，未變更的可以不用加入
}
```
return "store Card_ID not exist" or "updated"

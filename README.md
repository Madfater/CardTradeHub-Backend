# CardShop-Backend

## 測試POST 改後端資料庫成功

### HOW TO TEST

開MySQL 執行 [腳本](https://github.com/Madfater/CardShop/blob/backend_qq816/Backend/Sql_Init.txt)

Python套件記得裝

記得改MySQL密碼 [這裡](https://github.com/Madfater/CardShop/blob/backend_qq816/Backend/mysql.py)

執行[api.py](https://github.com/Madfater/CardShop/blob/backend_qq816/Backend/api.py)


測試用JSON檔


## request json format
### User
<details>
<summary>login</summary>

```python
# /login , method = GET
{
    "email": "123@gmail.com",
    "password": "passwd"
}
```
return "login success" or "login failed"
</details>



<details>
<summary>register</summary>

```python
# /register , method = POST
{
    "password": "passwd",
    "username": "alan",
    "email": "123@gmail.com"
}
```
return "User already exist" or "register success"
</details>

### Shopping Cart

<details>
<summary>GetShoppingCart</summary>

```python
# /get/shoppingCart/ , method = GET
{
    "User_ID" : 2,
    "page" : 1,
    "pageLimit" : 40
}
```
return StoreCard in ShoppingCart likes
```python
[
    [
        2,          # store card id
        15,         # price
        "舊卡新賣", # status
        20,         # quantity
        2,          # actual Card ID
        3           # store ID
    ]
]
```
</details>

### Store

<details>
<summary>GetStore(查詢store的所有 store Card)</summary>

```python
# /get/store/ , method = GET
{
    "Store_ID" : 1,
    "page" : 1,
    "pageLimit" : 40
}
```
return likes
```python
[
  [
    3,              # Card_id
    40,             # price
    "九成新狀態良好",# status
    15,             # quantity
    3,              # actual Card ID
    1               # store ID
  ],
  [
    4,
    500,
    "九成新狀態良好",
    10,
    4,
    1
  ]
]
```
</details>

### Store Card

<details>
<summary>searchCard (store Card)</summary>

```python
# /get/searchCard/ , method = GET
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
</details>



<details>
<summary>AddStoreCard</summary>

```python
# /add/storeCard/ , method = POST
{
    "price" : 100,
    "status" : "kinda new",
    "quantity" : 10,
    "ACCard_ID" : 1,
    "Store_ID" : 1
}
```
return "added"
</details>



<details>
<summary>updateStoreCard</summary>

```python
# /update/storeCard/ , method = PUT
{
    "Card_ID" : 1,    # storeCard ID 
    "price" : 114,
    "status" : "still new",
    "Quantity":514
    # 至少包含 price status Quantity其中一項，未變更的可以不用加入
}
```
return "store Card_ID not exist" or "updated"
</details>

<details>
<summary>RemoveCard</summary>

```python
# /remove/storeCard/ , method = DELETE
{
    "User_ID" : 2,
    "Card_ID" : 1
}
```
return "added"
</details>



### Actual Card

<details>
<summary>GetActualCard</summary>

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
</details>

<details>
<summary>AddActualCard</summary>

```python
# /add/actualCard/ , method = POST
{
    "name" : "nothing",
    "catagory" : "dragon",
    "description" : "destory enemy",
    "imgPath" : "http"
}
```
return "added"
</details>

<details>
<summary>updateActualCard</summary>

```python
# /update/actualCard/ , method = PUT
{
    "Card_ID" : 1,          # actual card id
    "name" : "forest elf",
    "catagory" : "elf",
    "description":"send itself to the tomb",
    "imgPath":"http:849898984"
    # 至少包含 name catagory description imgPath 其中一項，未變更的可以不用加入
}
```
return "ActualCard Card_ID not exist" or "updated"
</details>



### Comment

<details>
<summary>AddComment</summary>

```python
# /add/comment/ , method = POST
{
    "score" : 5,
    "context" : "777",
    "store_id" : 2,
    "user_id":1
}

```
return "added" or "add failed"
</details>

### Order
<details>
<summary>GetOrder</summary>

```python
# /get/order , method = GET
{
    "Order_id" : 102,
    "page" : 1,
    "pageLimit" : 40
}

```
return StoreCard likes
```python
[
    [
        5,
        15,
        "舊卡新賣",
        20,
        5,
        2
    ]
]
```
</details>

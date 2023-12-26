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
<summary>register</summary> 

```python
# /user/register , method = POST
{
    "password": "passwd",
    "username": "alan",
    "email": "123@gmail.com"
}
```
return "User already exist" or "register success"
</details>


<details>
<summary>login</summary>

```python
# /user/login , method = POST
{
    "email": "123@gmail.com",
    "password": "passwd"
}
```
return User ID or "login failed" or "this email isn't register yet"
</details>

<details>
<summary>Get User Name</summary>

```python
# /user/name?id=<int:user_id> , method = GET
# ex : /user/name?id=1
```
return User ID or "login failed" or "this email isn't register yet"
</details>

### Shopping Cart

<details>
<summary>check ShoppingCart</summary>

```python
# /cart?user_id=<int:user_id> , method = GET
# params可選包括 page (int), pageLimit (int)
# ex:/cart/user_id=1&page=1
```
return StoreCard in ShoppingCart likes
```python
{
  "items": {
    "2": [                # store id
      [
        1,               # store card id
        500,             # store card price
        "九成新狀態良好", # store card status
        10,              # store card quantity
        1,               # actual card id
        "青眼白龍",       # card name
        "怪獸卡",         # card category
        "超猛飛龍毀滅一切",# card description
        "https://imgur.com/a/2FFGPMs" # imgPath
      ],
      [
        3,
        40,
        "九成新狀態良好",
        15,
        3,
        "死者復甦",
        "法術卡",
        "復活墓地一隻怪獸卡到場上",
        "https://imgur.com/a/CYPu9TG"
      ]
    ]
  },
  "total_page": 1
}
```
</details>

<details>
<summary>Add Card To ShoppingCart</summary>


```python
# /cart/add , method = POST

{
    "user_id" : 1,
    "card_id" : 2
}
```
return "User not found" or "Card not found" or "added"
</details>

<details>
<summary>remove Card from ShoppingCart</summary>


```python
# /cart/remove , method = DELETE
{
    "user_id":1,
    "card_id":2
}
```
return "User not found" or "Card not found" or "Card not in shopping cart" or "removed"
</details>



### Store

<details>
<summary>check Store (查詢store的所有 store Card)</summary>

```python
# /store?id=<int:store_id> , method = GET
# params可選包括 page (int), pageLimit (int), orderWay (str)(包含 id, name, quantity), ascending(bool)
# ex:/store?id=1&page=1&ascending=true
```
return likes
```python
{
    "items": [
        [
            3,                          # Card_id
            40,                         # price
            "九成新狀態良好",            # status
            15,                         # quantity
            1,                          # actual card id
            "死者復甦",                  # name
            "法術卡",                    # catagory
            "復活墓地一隻怪獸卡到場上",    # description
            "https://imgur.com/a/CYPu9TG"# imgPath
        ],
        [
            4,
            500,
            "九成新狀態良好",
            10,
            1,
            "神聖彗星反射力量",
            "陷阱卡",
            "反射法術",
            "https://imgur.com/a/Dd7OHBt"
        ]
    ],
    "total_page": 1
}
```
</details>

### Actual Card

<details>
<summary>check ActualCard</summary>

```python
# /actualCard?id=<int:card_id> , method = GET
# ex: /actualCard?id=1
```
return "Card not found" or return ActualCard likes
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
<summary>Add ActualCard</summary>

```python
# /actualCard/add , method = POST
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
<summary>update ActualCard</summary>

```python
# /actualCard/update , method = PUT
{
    "card_id" : 1,
    "name" : "forest elf",
    "catagory" : "elf",
    "description":"send itself to the tomb",
    "imgPath":"http:849898984"
    # 至少包含 name catagory description imgPath 其中一項
}
```
return "Card not found" or "updated"
</details>

<details>
<summary>remove ActualCard</summary>

```python
# /actualCard/remove , method = DELETE
{
    "card_id":1
}
```
return "Card not found" or "removed"
</details>


### Comment

<details>
<summary>check comment from store</summary>

```python
# /comment?store_id=<int:store_id>&page=<int:page> , method = GET
# params可選包括 page (int), pageLimit (int)
# ex:/comment?store_id=1&page=1&pageLimit=30
```
return "Store not found" or return comment likes
```python
{
    "items": [
        [
            1,          # comment id
            5,          # score
            "賣家出貨快",# context
            1           # user id
        ]
    ],
    "total_page": 1
}
```
</details>

<details>
<summary>Add Comment</summary>

```python
# /comment/add , method = POST
{
    "store_id":1,
    "score" : 5,
    "context" : "777",
    "user_id":1
}

```
return "Store not found" or "User not found" or "added"
</details>

<details>
<summary>update Comment</summary>

```python
# /comment/update , method = PUT
{
    "comment_id" : 1
    "score" : 5,
    "context" : "777"
    # 至少包含 score context 其中一項
}

```
return "Comment not found" or "updated"
</details>

<details>
<summary>remove Comment</summary>

```python
# /comment/remove , method = DELETE
{
    "comment_id" : 1
}
```
return "Comment not found" or "removed"
</details>

### Order
</details>

<details>
<summary>check Order</summary>

```python
# /order?id=<int:order_id> , method = GET
# params可選包括 page (int), pageLimit (int)
# ex: /order?id=101&page=1
```
return "Order not found" or return Order likes
```python
{
    "items": {
        "1": [          # store id
            [
                4,              # store card id
                500,            # store card price
                4,              # order quantity
                4               # actual card id
            ]
        ]
    },
    "total_page": 1
}
```
</details>

<details>
<summary>add Order</summary>

```python
# /order/add , method = POST
{
    "user_id":1,
    "address":"",
    "items":{
        "2":1,
        "3":4
    }
}
```
return orderId
</details>

<details>
<summary>remove Order</summary>

```python
# /order/remove , method = DELETE
{
    'order_id':1
}
```
return "Order not found" or "removed"
</details>

### Store Card
<details>
<summary>get StoreCard</summary>

```python
# /card?id=<int:card_id> , method = POST
# ex: /card?id=1
```

return "Card not found" or return StoreCard likes
```python
[
    "神聖彗星反射力量",  # name
    "陷阱卡",           # catagory
    "反射法術",         # description
    500,                # price
    "九成新狀態良好",    # status
    10,                 # quantity
    4,                  # actual card id
    1,                  # store id
    "Happy Card Store"  # store name
]
```
</details>

<details>
<summary>search StoreCard</summary>

```python
# /card/search?keyword=<str:keyword> , method = GET
# params可選包括 page (int), pageLimit (int), orderWay (str)(包含 id, name, quantity), ascending(bool)
# ex: /card/search?keyword=卡&orderWay=price&ascending=false
```

return "no results" or return StoreCard likes
```python
{
    "items": [
        [
            5,              # store card id
            "貪欲之壺",      # name
            "法術卡",        # catagory
            "抽五張卡",      # description
            "https://imgur.com/a/pmltCFP", # img Path
            15,             # price
            "舊卡新賣",      # status
            20,             # quantity
            5,              # actual card id
            2,              # store id
            "Change Store"  # store name
        ],
        [
            3,
            "死者復甦",
            "法術卡",
            "復活墓地一隻怪獸卡到場上",
            "https://imgur.com/a/CYPu9TG",
            40,
            "九成新狀態良好",
            15,
            3,
            2,
            "Change Store"
        ]
    ],
    "total_page": 1
}
```
</details>

<details>
<summary>add StoreCard</summary>

```python
# /card/add , method = POST
{
    "store_id" : 1,
    "price":10,
    "status":"9成新",
    "quantity":4,
    "accard_ID": 2
}
```
return storeCard_ID or "Store not found"
</details>

<details>
<summary>update StoreCard</summary>

```python
# /card/update , method = POST
{
    "store_id" : 1,
    "price":10,
    "status":"9成新",
    "quantity":4
    # 至少包含 price status quantity 其中一個
}
```
return "Card not found" or "no access" or "updated"
</details>

<details>
<summary>remove StoreCard</summary>

```python
# /card/remove , method = POST
{
    "card_id":1,
    "user_id":1
}
```
return "Card not found" or "no access" or "updated"
</details>
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
return "login success" or "login failed" or "this email isn't register yet"
</details>


### Shopping Cart

<details>
<summary>check ShoppingCart (default)</summary>

```python
# /cart/user_id=<int:user_id> , method = GET
# ex: /cart/user_id=1

```
return StoreCard in ShoppingCart likes
```python
{
  "items": [
    [
      1,
      500,
      "九成新狀態良好",
      10,
      1,
      2
    ]
  ],
  "total_page": 1
}
```
</details>

<details>
<summary>check ShoppingCart</summary>

```python
# /cart/user_id=<int:user_id>&page=<int:page> , method = GET
# ex:/cart/user_id=1&page=1
# 每頁上限目前預設為 30
```
return StoreCard in ShoppingCart likes
```python
{
  "items": [
    [
      1,
      500,
      "九成新狀態良好",
      10,
      1,
      2
    ]
  ],
  "total_page": 1
}
```
</details>

<details>
<summary>Add Card To ShoppingCart</summary>


```python
# /cart/add/user_id=&card_id=<int:card_id> , method = POST
# ex:/cart/add/user_id=1&card_id=2
```
return "User not found" or "Card not found" or "added"
</details>

<details>
<summary>remove Card from ShoppingCart</summary>


```python
# /cart/remove/user_id=&card_id=<int:card_id> , method = DELETE
# ex:/cart/remove/user_id=1&card_id=2 
```
return "User not found" or "Card not found" or "Card not in shopping cart" or "removed"
</details>



### Store

<details>
<summary>check Store (查詢store的所有 store Card) (default)</summary>

```python
# /store/id=<int:store_id> , method = GET
# ex:/store/id=1
# 每頁上限目前預設為 30
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

<details>
<summary>check Store (查詢store的所有 store Card)</summary>

```python
# /store/id=<int:store_id>&page=<int:page> , method = POST
# ex:/store/id=1&page=1
# 每頁上限目前預設為 30
{
    "orderWay" : "id",  # 選項 : id, price, quantity
    "ascending" : true # true為正序
}
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
# /actualCard/id=<int:card_id> , method = GET
# ex: /actualCard/id=1
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
# /actualCard/update/id=<int:card_id> , method = PUT
# ex:/actualCard/update/id=1
{
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
# /actualCard/remove/id=<int:card_id> , method = DELETE
# ex:/actualCard/remove/id=1
```
return "Card not found" or "removed"
</details>


### Comment

<details>
<summary>check comment from store (default)</summary>

```python
# /comment/store_id=<int:store_id> , method = GET
# ex:/comment/store_id=1 
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
<summary>check comment from store</summary>

```python
# /comment/store_id=<int:store_id>&page=<int:page> , method = GET
# ex:/comment/store_id=1&page=1
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
# /comment/add/store_id=<int:store_id> , method = POST
# /comment/add/store_id=1
{
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
# /comment/update/id=<int:comment_id> , method = PUT
# /comment/update/id=1
{
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
# /comment/remove/id=<int:comment_id> , method = DELETE
# /comment/remove/id=1
```
return "Comment not found" or "removed"
</details>

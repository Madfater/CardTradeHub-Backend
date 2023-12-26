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
# /user/name?id=<int:userId> , method = GET
# ex : /user/name?id=1
```
return User ID or "login failed" or "this email isn't register yet"
</details>

### Shopping Cart

<details>
<summary>check ShoppingCart</summary>

```python
# /cart?userId=<int:userId> , method = GET
# params可選包括 page (int), pageLimit (int)
# ex:/cart/userId=1&page=1
```
return StoreCard in ShoppingCart likes
```python
{
    "items": {
        "2": [
            {
                "cardCategory": "怪獸卡",
                "cardDescription": "超猛飛龍毀滅一切",
                "cardName": "青眼白龍",
                "storeCardId": 1,
                "storeCardPrice": 500,
                "storeCardQuantity": 10,
                "storeCardStatus": "九成新狀態良好"
            },
            {
                "cardCategory": "法術卡",
                "cardDescription": "復活墓地一隻怪獸卡到場上",
                "cardName": "死者復甦",
                "storeCardId": 3,
                "storeCardPrice": 40,
                "storeCardQuantity": 15,
                "storeCardStatus": "九成新狀態良好"
            }
        ]
    },
    "totalPage": 1
}
```
</details>

<details>
<summary>Add Card To ShoppingCart</summary>


```python
# /cart/add , method = POST

{
    "userId" : 1,
    "cardId" : 2,
    "quantity" : 1
}
```
return "User not found" or "Card not found" or "added"
</details>

<details>
<summary>remove Card from ShoppingCart</summary>


```python
# /cart/remove , method = DELETE
{
    "userId":1,
    "cardId":2
}
```
return "User not found" or "Card not found" or "Card not in shopping cart" or "removed"
</details>



### Store

<details>
<summary>check Store</summary>

```python
# /store?id=<int:storeId> , method = GET
# ex:/store?id=1
```
return likes
```python
{
    "storeID": 1,
    "storeName": "Happy Card Store"
}
```
</details>

<details>
<summary>check Card in Store</summary>

```python
# /card/store?storeId=<int:storeId> , method = GET
# params可選包括 page (int), pageLimit (int), orderWay (str)(包含 id, name, quantity), ascending(bool)
# ex:/card/store?storeId=1&page=1&ascending=true
```
return likes
```python
{
    "items": [
        {
            "storeId": 1,
            "name": "神聖彗星反射力量",
            "actaulCardID": 4,
            "price": 500,
            "quantity": 10,
            "storeCardId": 4,
            "storeName": "Happy Card Store"
        },
        {
            "storeId": 1,
            "name": "黑魔導女孩",
            "actaulCardID": 2,
            "price": 10,
            "quantity": 4,
            "storeCardId": 7,
            "storeName": "Happy Card Store"
        }
    ],
    "totalPage": 1
}
```
</details>

### Actual Card

<details>
<summary>check ActualCard</summary>

```python
# /actualCard?id=<int:cardId> , method = GET
# ex: /actualCard?id=1
```
return "Card not found" or return ActualCard likes
```python
{
    "cardID":1,
    "name":"青眼白龍", 
    "catagory":"怪獸卡",
    "description":"超猛飛龍毀滅一切"
}
```
</details>

<details>
<summary>Add ActualCard</summary>

```python
# /actualCard/add , method = POST
{
    "name" : "nothing",
    "catagory" : "dragon",
    "description" : "destory enemy"
}
```
return "added"
</details>

<details>
<summary>update ActualCard</summary>

```python
# /actualCard/update , method = PUT
{
    "cardId" : 1,
    "name" : "forest elf",
    "catagory" : "elf",
    "description":"send itself to the tomb"
    # 至少包含 name catagory description 其中一項
}
```
return "Card not found" or "updated"
</details>

<details>
<summary>remove ActualCard</summary>

```python
# /actualCard/remove , method = DELETE
{
    "cardId":1
}
```
return "Card not found" or "removed"
</details>


### Comment

<details>
<summary>check comment from store</summary>

```python
# /comment?storeId=<int:storeId>&page=<int:page> , method = GET
# params可選包括 page (int), pageLimit (int)
# ex:/comment?storeId=1&page=1&pageLimit=30
```
return "Store not found" or return comment likes
```python
{
    "items": [
        {
            "commentID": 1,
            "context": "賣家出貨快",
            "score": 5,
            "userID": 1
        }
    ],
    "totalPage": 1
}
```
</details>

<details>
<summary>Add Comment</summary>

```python
# /comment/add , method = POST
{
    "storeId":1,
    "score" : 5,
    "context" : "777",
    "userId":1
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
# /order?id=<int:user_id> , method = GET
# params可選包括 page (int), pageLimit (int)
# ex: /order?id=1&page=1
```
return "Order not found" or return Order likes
```python
{
    "items": {
        "101": [ #訂單ID
            {
                "actualCardID": 4,
                "orderQuantity": 4,
                "storeCardID": 4,
                "storeCardPrice": 500,
                "storeID": 1
            }
        ],
        "104": [
            {
                "actualCardID": 2,
                "orderQuantity": 1,
                "storeCardID": 2,
                "storeCardPrice": 15,
                "storeID": 3
            },
            {
                "actualCardID": 3,
                "orderQuantity": 4,
                "storeCardID": 3,
                "storeCardPrice": 40,
                "storeID": 1
            }
        ]
    },
    "totalPage": 1
}
```
</details>

<details>
<summary>add Order</summary>

```python
# /order/add , method = POST
{
    "userId":1,
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
# /card?id=<int:cardId> , method = POST
# ex: /card?id=1
```

return "Card not found" or return StoreCard likes
```python
{
    "actaulCardID": 4,
    "name": "神聖彗星反射力量",
    "price": 500,
    "quantity": 10,
    "storeCardId": 4,
    "storeId": 1,
    "storeName": "Happy Card Store"
}
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
        {
            "actaulCardID": 5,
            "name": "貪欲之壺",
            "price": 15,
            "quantity": 20,
            "storeCardId": 5,
            "storeId": 2,
            "storeName": "Change Store"
        },
        {
            "actaulCardID": 3,
            "name": "死者復甦",
            "price": 40,
            "quantity": 15,
            "storeCardId": 3,
            "storeId": 2,
            "storeName": "Change Store"
        }
    ],
    "totalPage": 1
}
```
</details>

<details>
<summary>add StoreCard</summary>

```python
# /card/add , method = POST
{
    "storeId" : 1,
    "price":10,
    "status":"9成新",
    "quantity":4,
    "accardId": 2
}
```
return storecardId or "Store not found"
</details>

<details>
<summary>update StoreCard</summary>

```python
# /card/update , method = POST
{
    "storeId" : 1,
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
    "cardId":1,
    "userId":1
}
```
return "Card not found" or "no access" or "updated"
</details>
from flask import Flask, jsonify, request
from structure import card,cart,order,store,user,comment
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# User
@app.route('/user/<path:method>', methods = ['POST'])
def UserApproach(method):
    if method == "login":
        return jsonify(user.Login(request.get_json()))
    elif method == "register":
        return jsonify(user.Register(request.get_json()))
@app.route('/user/name', methods = ['GET'])
def GetUserName():
    id = request.args.get('id')
    return jsonify(user.GetName(id))

# ShoppingCart
@app.route('/cart', methods = ['GET'])
def Cart():
    user_id = request.args.get('user_id')
    page = request.args.get('page', default = 1, type = int)
    pageLimit = request.args.get('page_limit', default = 30, type = int)
    return jsonify(cart.lookCart(user_id,page,pageLimit))
@app.route('/cart/add', methods = ['POST'])
def AddCardToCart():
    return jsonify(cart.addCard(request.get_json()))
@app.route('/cart/remove', methods = ['DELETE'])
def RemoveCardFromCart():
    return jsonify(cart.removeCard(request.get_json()))

# Store
@app.route('/store', methods = ['GET'])
def Store():
    store_id = request.args.get('id')
    page = request.args.get('page', default = 1, type = int)
    pageLimit = request.args.get('pageLimit', default = 30, type = int)
    orderWay = request.args.get('orderWay', default = "id", type = str)
    ascending = request.args.get('ascending', default = True, type = bool)
    return jsonify(store.lookStore(store_id, page, pageLimit, orderWay, ascending))

# Actual Card
@app.route('/actualCard', methods = ['GET'])
def ActualCard():
    card_id = request.args.get('id')
    return jsonify(card.GetActualCard(card_id))
@app.route('/actualCard/add', methods = ['POST'])
def AddActualCard():
    return jsonify(card.AddActualCard(request.get_json()))
@app.route('/actualCard/update', methods = ['PUT'])
def UpdateActualCard():
    return jsonify(card.updateActualCard(request.get_json()))
@app.route('/actualCard/remove', methods = ['DELETE'])
def RemoveActualCard():
    return jsonify(card.removeActualCard(request.get_json()))

# comment
@app.route('/comment', methods = ['GET'])
def Comment():
    store_id = request.args.get('store_id')
    page = request.args.get('page', default = 1 , type = int)
    pageLimit = request.args.get('pageLimit', default = 30 , type = int)
    return jsonify(comment.lookComment(store_id,page,pageLimit))
@app.route('/comment/add', methods = ['POST'])
def AddComment():
    return jsonify(comment.AddComment(request.get_json()))
@app.route('/comment/update', methods = ['PUT'])
def UpdateComment():
    return jsonify(comment.updateComment(request.get_json()))
@app.route('/comment/remove', methods = ['DELETE'])
def RemoveComment():
    return jsonify(comment.removeComment(request.get_json()))

# order
@app.route('/order', methods = ['GET'])
def Order():
    id = request.args.get('id')
    page = request.args.get('page', default = 1 , type = int)
    pageLimit = request.args.get('pageLimit', default = 30 , type = int)
    return jsonify(order.lookOrder(id, page, pageLimit))
@app.route('/order/add', methods = ['POST'])
def AddOrder():
    return jsonify(order.addOrder(request.get_json()))
@app.route('/order/remove', methods = ['DELETE'])
def RemoveOrder():
    return jsonify(order.removeOrder(request.get_json()))

# Store Card
@app.route('/card', methods = ['GET'])
def Card():
    id = request.args.get('id')
    return jsonify(card.GetStoreCard(id))
@app.route('/card/search', methods = ['GET'])
def SearchCard():
    param = request.args.get('keyword')
    page = request.args.get('page', default = 1, type = int)
    pageLimit = request.args.get('pageLimit', default = 30, type = int)
    orderWay = request.args.get('orderWay', default = "id", type = str)
    ascending = request.args.get('ascending', default = True, type = bool)
    return jsonify(card.searchStoreCard(param, page, pageLimit, orderWay, ascending))
@app.route('/card/add', methods = ['POST'])
def AddCard():
    return jsonify(card.AddStoreCard(request.get_json()))
@app.route('/card/update', methods = ['PUT'])
def UpdateCard():
    return jsonify(card.UpdateCard(request.get_json()))
@app.route('/card/remove', methods = ['DELETE'])
def RemoveCard():
    return jsonify(card.removeStoreCard(request.get_json()))

if __name__ == '__main__':
    app.run(debug = True, host=0.0.0.0)
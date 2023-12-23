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

# ShoppingCart
@app.route('/cart/user_id=<int:user_id>', methods = ['GET'])
def CartDefault(user_id):
    return jsonify(cart.lookCart(user_id))
@app.route('/cart/user_id=<int:user_id>&page=<int:page>', methods = ['GET'])
def Cart(user_id,page):
    return jsonify(cart.lookCart(user_id,page,pageLimit=30))
@app.route('/cart/add/user_id=<int:user_id>&card_id=<int:card_id>', methods = ['POST'])
def AddCardToCart(user_id, card_id):
    return jsonify(cart.addCard(user_id,card_id))
@app.route('/cart/remove/user_id=<int:user_id>&card_id=<int:card_id>', methods = ['DELETE'])
def RemoveCardFromCart(user_id, card_id):
    return jsonify(cart.removeCard(user_id, card_id))

# Store
@app.route('/store/id=<int:store_id>', methods = ['GET'])
def StoreDefault(store_id):
    return jsonify(store.lookStore(store_id))
@app.route('/store/id=<int:store_id>&page=<int:page>', methods = ['POST'])
def Store(store_id,page):
    return jsonify(store.lookStore(store_id, request.get_json(),page))

# Actual Card
@app.route('/actualCard/id=<int:card_id>', methods = ['GET'])
def ActualCard(card_id):
    return jsonify(card.GetActualCard(card_id))
@app.route('/actualCard/add', methods = ['POST'])
def AddActualCard():
    return jsonify(card.AddActualCard(request.get_json()))
@app.route('/actualCard/update/id=<int:card_id>', methods = ['PUT'])
def UpdateActualCard(card_id):
    return jsonify(card.updateActualCard(card_id,request.get_json()))
@app.route('/actualCard/remove/id=<int:card_id>', methods = ['DELETE'])
def RemoveActualCard(card_id):
    return jsonify(card.removeActualCard(card_id))

# comment
@app.route('/comment/store_id=<int:store_id>', methods = ['GET'])
def CommentDefault(store_id):
    return jsonify(comment.lookComment(store_id))
@app.route('/comment/store_id=<int:store_id>&page=<int:page>', methods = ['GET'])
def Comment(store_id,page):
    return jsonify(comment.lookComment(store_id,page))
@app.route('/comment/add/store_id=<int:store_id>', methods = ['POST'])
def AddComment(store_id):
    return jsonify(comment.AddComment(store_id, request.get_json()))
@app.route('/comment/update/id=<int:comment_id>', methods = ['PUT'])
def UpdateComment(comment_id):
    return jsonify(comment.updateComment(comment_id, request.get_json()))
@app.route('/comment/remove/id=<int:comment_id>', methods = ['DELETE'])
def RemoveComment(comment_id):
    return jsonify(comment.removeComment(comment_id))


if __name__ == '__main__':
    app.run(debug = True)
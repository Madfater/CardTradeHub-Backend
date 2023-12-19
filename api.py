from flask import Flask, jsonify, request
import structure.card as card
import structure.cart as cart
import structure.order as order
import structure.store as store
import structure.user as user
import structure.order as order
import structure.comment as comment
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get/<path>/', methods=['GET'])
def GetMethod(path):
    result = None
    if path == "searchCard":
        result = card.searchCard(request.get_json())
    elif path == "actualCard":
        result = card.GetActualCard(request.get_json())
    elif path == "shoppingCart":
        result = cart.GetCart(request.get_json())
    elif path == "store":
        result = store.GetStore(request.get_json())
    elif path == "order":
        result = order.GetOrder(request.get_json())
    
    return jsonify(result)

@app.route('/login', methods=['GET'])
def login():
    return jsonify(user.loginUser(request.get_json()))

@app.route('/register', methods=['POST'])
def register():
    result = user.registerUser(request.get_json())
    return jsonify(result)

@app.route('/add/<path>/', methods=['POST'])
def AddMethod(path):
    result = None
    if path == "comment":
        result = comment.AddComment(request.get_json())
    elif path == "storeCard":
        result = card.AddCard(request.get_json())
    return jsonify(result)

@app.route('/update', methods=['PUT'])
def Update():
    result = card.updateCard(request.get_json())
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug = True)
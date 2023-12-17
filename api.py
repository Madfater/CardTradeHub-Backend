from flask import Flask, jsonify, request
import mysql as sql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get/<path>/', methods=['GET'])
def GetMethod(path):
    result = None
    if path == "storeCard":
        result = sql.GetCard(request.get_json())
    elif path == "actualCard":
        result = sql.GetActualCard(request.get_json())
    elif path == "shoppingCart":
        result = sql.GetCart(request.get_json())
    elif path == "store":
        result = sql.GetStore(request.get_json())
    return jsonify(result)

@app.route('/login', methods=['GET'])
def login():
    return jsonify(sql.loginUser(request.get_json()))

@app.route('/register', methods=['POST'])
def register():
    result = sql.registerUser(request.get_json())
    return jsonify(result)

@app.route('/update', methods=['PUT'])
def Update():
    result = sql.updateCard(request.get_json())
    return jsonify(result)

'''@app.route('/api/user')
def renderHtml():
    return render_template('home.html')'''

if __name__ == '__main__':
    app.run(debug = True)
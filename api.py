from flask import Flask, jsonify, request
import mysql as sql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/user', methods=['GET'])
def get_user_info():
    return jsonify("yes get")

@app.route('/login', methods=['POST'])
def login():
    result = sql.loginUser(request.get_json())
    return jsonify(result)

@app.route('/register', methods=['POST'])
def login():
    result = sql.registerUser(request.get_json())
    return jsonify(result)

@app.route('/api/user', methods=['POST'])
def submit_user_info():
    result = sql.manageCommand(request.get_json())
    return jsonify(result)

'''@app.route('/api/user')
def renderHtml():
    return render_template('home.html')'''

if __name__ == '__main__':
    app.run(debug = True)
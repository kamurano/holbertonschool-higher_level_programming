#!/usr/bin/python3
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def data():
    usernames = users.keys()
    return jsonify(usernames)

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        user = request.get_json()
        users[user['name']] = user
        return jsonify({"message": "User added", user['name'] : user})
        

@app.route('/users/<username>')
def user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run()

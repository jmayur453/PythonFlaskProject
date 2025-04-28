from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from app.db import users_db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users_db and users_db[username] == password:
        return jsonify({"success": True})
    
    return jsonify({"success": False, "message": "Invalid username or password!"})

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users_db:
        return jsonify({"success": False, "message": "Username already taken!"})
    
    users_db[username] = password
    return jsonify({"success": True})


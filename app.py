from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from model import calculate_nutrition
import os
import mysql.connector

app = Flask(__name__)
CORS(app)

# #  MySQL 
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="1234",
#     database="Diet"
# )

# cursor = conn.cursor()
if os.environ.get("RENDER"):
    # 🌐 Running on Render → use SQLite
    import sqlite3
    conn = sqlite3.connect('diet.db', check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
    ''')

    conn.commit()

else:
    # 💻 Running locally → use MySQL
    import mysql.connector
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="Diet"
    )
    cursor = conn.cursor()

#  PART  ADD
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login-page')
def login_page():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data['email']
    password = data['password']
    if os.environ.get("RENDER"):
        cursor.execute("SELECT id,name FROM users WHERE email=? AND password=?", (email, password))
    else:
        cursor.execute("SELECT id,name FROM users WHERE email=%s AND password=%s", (email, password))

    # query = "SELECT id, name FROM users WHERE email=%s AND password=%s"
    # cursor.execute(query, (email, password))
    user = cursor.fetchone()

    if user:
        return jsonify({
            "user_id": user[0],
            "name": user[1]
        })
    else:
        return jsonify({"error": "Invalid login"})
@app.route('/history-page')
def history_page():
    return render_template("history.html")

@app.route('/profile-page')
def profile_page():
    return render_template("profile.html")


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    
    weight = data['weight']
    foods = data['foods']

    result = calculate_nutrition(weight, foods)

    return jsonify(result)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    name = data['name']
    email = data['email']
    password = data['password']

    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    
    try:
        cursor.execute(query, (name, email, password))
        conn.commit()
        return jsonify({"message": "User registered"})
    except:
        return jsonify({"error": "Email already exists"})







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

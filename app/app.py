# app/app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
import os

app = Flask(__name__)

DB_HOST = os.getenv("MYSQL_HOST", "mysql")
DB_USER = os.getenv("MYSQL_USER", "root")
DB_PASS = os.getenv("MYSQL_PASSWORD", "password")
DB_NAME = os.getenv("MYSQL_DATABASE", "inventorydb")

def get_db_conn():
    return mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME
    )

@app.route("/")
def index():
    conn = get_db_conn()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT id, name, qty FROM items ORDER BY id DESC")
    items = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", items=items)

@app.route("/add", methods=["POST"])
def add_item():
    name = request.form.get("name")
    qty = int(request.form.get("qty", 0))
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name, qty) VALUES (%s, %s)", (name, qty))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for("index"))

@app.route("/api/items", methods=["GET"])
def api_items():
    conn = get_db_conn()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT id, name, qty FROM items ORDER BY id DESC")
    items = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


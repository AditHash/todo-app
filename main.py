from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os
import uuid
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")

# MongoDB setup
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)
db = client["crud_db"]
collection = db["todos"]
users_collection = db["users"]

# Ensure index on 'id' field
collection.create_index("id", unique=True)

@app.route("/")
def index():
    if "user" not in session:
        return redirect(url_for("login"))
    todos = list(collection.find({"user": session["user"]}))
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add_todo():
    if "user" not in session:
        return redirect(url_for("login"))
    topic = request.form["topic"]
    description = request.form["description"]
    due_date = request.form["due_date"]
    priority = request.form["priority"]
    if topic and description:
        collection.insert_one({
            "id": str(uuid.uuid4()),
            "topic": topic,
            "description": description,
            "due_date": due_date,
            "priority": priority,
            "completed": False,
            "user": session["user"]
        })
    return redirect(url_for("index"))

@app.route("/edit/<id>")
def edit_todo(id):
    if "user" not in session:
        return redirect(url_for("login"))
    todo = collection.find_one({"id": id, "user": session["user"]})
    return render_template("edit.html", todo=todo)

@app.route("/update/<id>", methods=["POST"])
def update_todo(id):
    if "user" not in session:
        return redirect(url_for("login"))
    topic = request.form["topic"]
    description = request.form["description"]
    due_date = request.form["due_date"]
    priority = request.form["priority"]
    completed = "completed" in request.form
    collection.update_one(
        {"id": id, "user": session["user"]},
        {"$set": {"topic": topic, "description": description, "due_date": due_date, "priority": priority, "completed": completed}}
    )
    return redirect(url_for("index"))

@app.route("/delete/<id>")
def delete_todo(id):
    if "user" not in session:
        return redirect(url_for("login"))
    collection.delete_one({"id": id, "user": session["user"]})
    return redirect(url_for("index"))

@app.route("/toggle_complete/<id>")
def toggle_complete(id):
    if "user" not in session:
        return redirect(url_for("login"))
    todo = collection.find_one({"id": id, "user": session["user"]})
    if todo:
        collection.update_one({"id": id}, {"$set": {"completed": not todo["completed"]}})
    return redirect(url_for("index"))

@app.route("/api/todos", methods=["GET", "POST"])
def api_todos():
    if request.method == "GET":
        todos = list(collection.find({"user": session.get("user", None)}, {"_id": 0}))
        return jsonify(todos)
    elif request.method == "POST":
        data = request.json
        data["id"] = str(uuid.uuid4())
        data["user"] = session.get("user", None)
        collection.insert_one(data)
        return jsonify({"message": "Todo added"}), 201

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = users_collection.find_one({"username": username})
        if user and check_password_hash(user["password"], password):
            session["user"] = username
            return redirect(url_for("index"))
        return "Invalid credentials", 401
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        users_collection.insert_one({"username": username, "password": password})
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/health")
def health_check():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

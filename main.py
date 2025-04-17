from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
import uuid

app = Flask(__name__)

# MongoDB setup
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)
db = client["crud_db"]
collection = db["todos"]

# Ensure index on 'id' field
collection.create_index("id", unique=True)

@app.route("/")
def index():
    todos = list(collection.find())
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add_todo():
    topic = request.form["topic"]
    description = request.form["description"]
    if topic and description:
        collection.insert_one({
            "id": str(uuid.uuid4()),
            "topic": topic,
            "description": description
        })
    return redirect(url_for("index"))

@app.route("/edit/<id>")
def edit_todo(id):
    todo = collection.find_one({"id": id})
    return render_template("edit.html", todo=todo)

@app.route("/update/<id>", methods=["POST"])
def update_todo(id):
    topic = request.form["topic"]
    description = request.form["description"]
    collection.update_one(
        {"id": id},
        {"$set": {"topic": topic, "description": description}}
    )
    return redirect(url_for("index"))

@app.route("/delete/<id>")
def delete_todo(id):
    collection.delete_one({"id": id})
    return redirect(url_for("index"))

@app.route("/health")
def health_check():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

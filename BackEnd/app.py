import sys
import os
import db
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from db import insert_client, get_clients

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("DB FILE LOADED FROM:", db.__file__)

print("APP STARTED...")

print(os.listdir("templates")) # Checks if this file exists through the run

# Flask API:

app = Flask(__name__)
CORS(app)

@app.before_request
def log():
    print("REQUEST:", request.method, request.path)

@app.route('/')
def home():
    return render_template('index.html')

# GET all clients

@app.route('/api/clients', methods=['GET'])
def fetch_clients():
    try:
        data = get_clients()
        print("DATA:", data)
        return jsonify(data)
    except Exception as e:
        print("FULL ERROR:", e)
        return jsonify({"error": str(e)}), 500


# POST new client
@app.route('/api/clients', methods=['POST'])
def add_client():
    data = request.json
    insert_client(data)
    return jsonify({"message": "Client added successfully"}), 201
    print("Incoming JSON:", data) # Debug print <<<<<


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
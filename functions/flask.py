from flask import Flask, jsonify
from netlify import handler

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask running on Netlify!"

# Wrap the Flask app in a Netlify handler
handler(app)

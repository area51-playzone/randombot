from flask import Flask, render_template, jsonify, request
import requests
app = Flask(__name__,static_folder='assets')

@app.route('/')
def hello_world():
    return render_template('home.html')

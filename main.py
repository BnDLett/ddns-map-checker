from flask import Flask, redirect, url_for, render_template, request
from socket import socket, create_connection, AF_INET, SOCK_DGRAM
from struct import unpack
from time import time
import threading

Port = 1000
print(Port)

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template("index.html", a1="Unknown")
print(1)

@app.route('/', methods=['POST'])
def index_post():
    text = request.form['text']
    try:
        with open('maps.txt', 'r') as x:
            x = x.read()
            y = text.lower() in x.lower()
    except Exception as e:
        y = f"A fatal error has occured: {e}"
    return render_template("index.html", a1=y)
print(2)

@app.route("/secondary")
def secondary():
    return render_template("old_index.html", a1="Unknown")
print(3)
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=Port)

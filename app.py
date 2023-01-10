from flask import Flask, redirect, url_for, render_template, request
from socket import socket, create_connection, AF_INET, SOCK_DGRAM
from struct import unpack
from time import time
import threading

class Server():
    def __init__(self, host, server_port = 6567, socketinput_port = 6859):
        self.host = host
        self.server = (host, server_port)
        self.socketinput_port = socketinput_port
        
    def get_status(self):
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(self.server)
        s.send(b"\xfe\x01")
    
        statusdict = {}
    
        data = s.recv(1024)
        statusdict["name"] = data[1:data[0]+1].decode("utf-8")
        data = data[data[0]+1:]
        statusdict["map"] = data[1:data[0]+1].decode("utf-8")
        data = data[data[0]+1:]
        statusdict["players"] = unpack(">i", data[:4])[0]
        data = data[4:]
        statusdict["wave"] = unpack(">i", data[:4])[0]
        data = data[4:]
        statusdict["version"] = unpack(">i", data[:4])[0]
        data = data[4:]
        statusdict["vertype"] = data[1:data[0]+1].decode("utf-8")
        
        return statusdict

app = Flask(__name__, static_url_path='/static')


def mapthingy():
    while True:
        for i in range(4):
            server = Server("mindustry.ddns.net", 1000*(i+1))
            z = server.get_status()["map"]
            with open('maps.txt', 'r') as x:
                x = x.read()
                with open('maps.txt', 'a') as y:
                    if z.lower() not in x.lower():
                        y.write(f"{z}\n")

x = threading.Thread(None, mapthingy, None)
x.start()

@app.route("/")
def home():
    return render_template("index.html", a1="Unknown")

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

@app.route("/secondary")
def secondary():
    return render_template("old_index.html", a1="Unknown")

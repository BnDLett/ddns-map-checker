import websocket, time

while True:
    ws = websocket.WebSocket()
    ws.connect('https://mdnmapcheck.ddns.net', header=["User-Agent: MyProgram", "x-custom: header"])
    ws.send("Test")
    print(ws.recv())
    time.sleep(5)
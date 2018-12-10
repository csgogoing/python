import websocket
import websocket
try:
	import thread
except ImportError:
	import _thread as thread
import time
import json

def on_message(ws, message):
	print(message)
	if json.loads(message)['act'] == "PING":
		ws.send('{"act":"PONG"}')

def on_error(ws, error):
	print(error)

def on_close(ws):
	print("### closed ###")

def on_open(ws):
	ws.send('{"userid": "68258667", "act": "CONNECT"}')


if __name__ == "__main__":
	websocket.enableTrace(True)
	ws = websocket.WebSocketApp("ws://10.20.4.22:8078/websocket",on_message = on_message,on_error = on_error,on_close = on_close)
	ws.on_open = on_open
	ws.run_forever()
	ws.send('{"from": "68258667","to": "333","id": "%d","body": {"content": "回复内容","qid": "15339"},"act": "PUB"}'%int(round(time.time() * 1000)))


{"act":"PUB","body":{"time":1544436201,"type":101002,"qid":15339,"user_photo":"http://test.d.xywy.com/im-static/images/18-40-1.png","content":{"text":"追问内容11","type":"text"}},"from":"117333204","id":"61605","seq":1,"to":"68258667"}
{"act":"PUB","body":{"time":1544436220,"type":101002,"qid":15339,"user_photo":"http://test.d.xywy.com/im-static/images/18-40-1.png","content":{"text":"追问内容22","type":"text"}},"from":"117333204","id":"61606","seq":2,"to":"68258667"}

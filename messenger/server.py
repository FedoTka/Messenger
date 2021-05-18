from flask import Flask, request,Response
from datetime import datetime, timezone
import time 

app = Flask(__name__)

messages=[
	#{'name':'Mary','time':time.time(),'text':'Привет'},
	#{'name':'Ma','time':time.time(),'text':'hello'},
]

@app.route("/send", methods=['POST'])
def send():

	name=request.json.get('name')
	text=request.json.get('text')

	if not name or not text:
		return Response(status=400)
	message={'name':name,'time':time.time(),'text':text}
	messages.append(message)
	
	return Response(status=200)

def filter_by_key(elements, key,threshold):
	
	filtered_elements=[]

	for element in elements:
		if element[key]>threshold:
			filtered_elements.append(element)

	
	return filtered_elements		



@app.route("/messages")
def messages_view():
	try:
		after=float(request.args['after'])
	except:
		return Response(status=400)
			
	filtered=filter_by_key(messages, key='time',threshold=after)
	return {'messages':filtered}


@app.route("/status")
def status():
    return {
     	'status':"True",
     	'name':"LoH",
     	'time':datetime.now(),

    }



app.run()    
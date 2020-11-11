from flask import Blueprint
from flask import render_template
from flask import request
import requests
import json
import sys
sys.path.append('../database')
sys.path.append('..')
import db

frontend_app = Blueprint('frontend_app', __name__)


@frontend_app.route('/', methods=['GET','POST'])
def home_page():
	insert_msg = ""
	delete_msg = ""
	if request.method == 'POST':
		print(request.form);
		type1 = request.form.get('ltype')
		receiver = request.form.get('lreceiver')
		date = request.form.get('ldate')
		time = request.form.get('ltime')
		message = request.form.get('lmessage')
		link = request.base_url  + '/api/agendamentos?'
		link += "type_id="+str(type1)
		link += "&receiver_id="+str(receiver)
		link += "&date_time="+str(date)+" "+str(time)
		link += "&message="+str(message)
		insert_msg = requests.post(link).text
		print(type1,receiver,date,time,message);
		print(link);
	elif request.method == 'DELETE':
		
	types = json.loads(db.select("SELECT id, type from send_type"))
	receivers = json.loads(db.select("SELECT id, name from receiver"))
	send_schedule = json.loads(requests.get(request.base_url  + '/api/agendamentos').text)
	return render_template('home_page.html', types=types, receivers=receivers,send_schedule=send_schedule,insert_msg=insert_msg, delete_msg=delete_msg)


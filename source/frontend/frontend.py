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
		insert_msg = "entrou no post"
		#todo
	types = json.loads(db.select("SELECT id, type from send_type"))
	receivers = json.loads(db.select("SELECT id, name from receiver"))
	send_schedule = json.loads(requests.get(request.base_url  + '/api/agendamentos').text)
	return render_template('home_page.html', types=types, receivers=receivers,send_schedule=send_schedule,insert_msg=insert_msg, delete_msg=delete_msg)


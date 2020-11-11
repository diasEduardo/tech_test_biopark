from flask import Blueprint
from flask import render_template
from flask import request
import json
import sys
sys.path.append('../database')
sys.path.append('..')
import db
from index import app

frontend_app = Blueprint('frontend_app', __name__)


@frontend_app.route('/', methods=['GET','POST'])
def home_page():
	if request.method == 'POST':
		a=1
	types = json.loads(db.select("SELECT id, type from send_type"))
	receivers = json.loads(db.select("SELECT id, name from receiver"))
	#send_schedule = json.loads(app.get('/api/agendamentos'))
	print(send_schedule)
	return render_template('home_page.html', types=types, receivers=receivers,send_schedule=send_schedule)


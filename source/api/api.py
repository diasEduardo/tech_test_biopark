from flask import Flask
from flask import request
import sys
sys.path.append('../database')
import db

app = Flask(__name__)

@app.route('/api/agendamentos',methods=['GET'])
def list_all_schedule():
	query = "SELECT s.id, st.status, t.type, r.name, r.email, r.phone, s.date_time, s.message "\
			"FROM send_schedule AS s "\
			"JOIN send_status AS st ON s.status_id = st.id "\
			"JOIN send_type AS t ON s.type_id = t.id "\
			"JOIN receiver AS r ON s.receiver_id = r.id "
	response = db.select(query);
	return response

@app.route('/api/agendamentos/<select_id>',methods=['GET'])
def select_schedule(select_id):
	query = "SELECT s.id, st.status, t.type, r.name, r.email, r.phone, s.date_time, s.message "\
			"FROM send_schedule AS s "\
			"JOIN send_status AS st ON s.status_id = st.id "\
			"JOIN send_type AS t ON s.type_id = t.id "\
			"JOIN receiver AS r ON s.receiver_id = r.id "\
			"WHERE s.id = " + str(select_id)
	response = db.select(query);
	return response

@app.route('/api/agendamentos',methods=['POST'])
def insert_schedule():
	output = "erro ao inserir"
	code = 400
	erro_flag = False

	status  = 1
	type1 = int(request.args.get('type_id'))
	receiver = int(request.args.get('receiver_id'))
	date = request.args.get('date_time')
	message = request.args.get('message')
	if(type1 is None):
		erro_flag = True 
	elif(receiver is None):
		erro_flag = True
	elif(date is None):
		erro_flag = True
	elif(message is None):
		message = ""
	

	if( not erro_flag):
		query = "INSERT INTO send_schedule(status_id,type_id,receiver_id,date_time,message) "\
			"values(%d, %d, %d, '%s', '%s')"%(status, type1, receiver, date, message)
		response = db.exec(query);
		if(response):
			output = "inserido com sucesso"
			code = 200

	return output, code

@app.route('/api/agendamentos/<delete_id>',methods=['DELETE'])
def delete_schedule(delete_id):
	output = "erro ao deletar o agendamento"
	code = 500
	query = "DELETE FROM send_schedule "\
			"WHERE id = " + str(delete_id)
	response = db.exec(query)

	if(response):
		output = "O agendamento foi deletado"
		code = 200	
	
	return output, code



app.run()
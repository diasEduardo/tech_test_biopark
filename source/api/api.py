from flask import Flask
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
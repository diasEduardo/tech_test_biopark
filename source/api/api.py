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
	response = db.exec(query);
	return response

@app.route('/api/agendamentos/<delete_id>',methods=['DELETE'])
def delete_schedule(delete_id):
	query = "DELETE FROM send_schedule "\
			"WHERE id = " + str(delete_id)
	print(query)
	response = db.exec(query)
	print(response)
	return response



app.run()
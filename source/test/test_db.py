import sys
sys.path.append('../database')
import db
import json

def test_db():
	#select
	assert db.select("SELECT version()") != None
	assert db.select("SELECT id FROM send_type LIMIT 1") != None
	assert db.select("SELECT id FROM send_status LIMIT 1") != None
	assert db.select("SELECT id FROM send_schedule LIMIT 1") != None
	assert db.select("SELECT id FROM receiver LIMIT 1") != None
	assert db.select("SELECT id, date_time FROM send_schedule LIMIT 1") != None

	#insert
	query = "INSERT INTO send_schedule(status_id,type_id,receiver_id,date_time,message) "\
			"values(%d, %d, %d, '%s', '%s')"%( 4, 4, 1, '2020-12-21 11:00:54', "auto teste")
	insert = db.exec(query)
	assert insert > 0
	response = json.loads(db.select("SELECT id FROM send_schedule ORDER BY id DESC LIMIT 1 "))
	#delete
	delete = db.exec("DELETE FROM send_schedule where id = "+str(response[0]['id']))
	assert delete == 0 or delete == 1

test_db();
print("test_db pass")
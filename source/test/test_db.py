import sys
sys.path.append('../database')
import db

def test_db():
	#select
	assert db.select("SELECT version()") != None
	assert db.select("SELECT id FROM send_type LIMIT 1") != None
	assert db.select("SELECT id FROM send_status LIMIT 1") != None
	assert db.select("SELECT id FROM send_schedule LIMIT 1") != None
	assert db.select("SELECT id FROM receiver LIMIT 1") != None
	assert db.select("SELECT id, date_time FROM send_schedule LIMIT 1") != None

	#insert
	id = 15
	#delete
	delete = db.exec("DELETE FROM send_schedule where id = "+str(id))
	assert delete == 0 || delete == 1

test_db();
print("test_db pass")
import sys
sys.path.append('../database')
import db

def test_db():
	assert db.exec("SELECT version()") != None
	assert db.exec("SELECT id FROM send_type LIMIT 1") != None
	assert db.exec("SELECT id FROM send_status LIMIT 1") != None
	assert db.exec("SELECT id FROM send_schedule LIMIT 1") != None
	assert db.exec("SELECT id FROM receiver LIMIT 1") != None

test_db();
print("test_db pass")

import sys
sys.path.append('../api')
import api
import json
from flask import Flask
import db

def client():
	app = api.app
	app.testing = True
	return app.test_client()

def test_get_schedule():
	tester = client()
	
	rv = tester.get('/api/agendamentos')
	assert rv != None

	rv = tester.get('/api/agendamentos/0')
	assert rv != None

def test_post_schedule():
	tester = client()
	rv = tester.post('/api/agendamentos')
	
	assert rv.data == b'erro ao inserir, valores incorretos'
	rv = tester.post('/api/agendamentos')
	assert rv.data == b'erro ao inserir, valores incorretos'
	rv = tester.post('/api/agendamentos?type_id=1&receiver_id=1&date_time=2020-12-21 11:00:00')
	assert rv.data == b'erro ao inserir, valores incorretos'
	rv = tester.post('/api/agendamentos?type_id=1&receiver_id=1&date_time=2020-12-21 11:00:00&message=msg')
	assert rv.data == b'inserido com sucesso'
	response = json.loads(db.select("SELECT id FROM send_schedule ORDER BY id DESC LIMIT 1 "))
	return response[0]['id'];

def test_delete_schedule(id_test):
	tester = client()
	rv = tester.delete('/api/agendamentos/'+str(id_test))
	assert rv.data != None
	rv = tester.delete('/api/agendamentos/'+str(id_test))
	assert rv.data == b'erro ao deletar o agendamento' or rv == b'O agendamento foi deletado'

test_get_schedule();
id_test = test_post_schedule();
test_delete_schedule(id_test);
print("test_api_route pass")
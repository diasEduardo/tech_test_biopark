import psycopg2
import sys
sys.path.append('../utils')
from config_parser import config

params = config("C:\\Users\\Eduardo\\Documents\\git_projects\\tech_test_biopark\\source\\database\\db.ini","postgresql")

def exec(query):
	conn = None
	query_response = None
	try:
		
		conn = psycopg2.connect(**params)
		
		cur = conn.cursor()
		cur.execute(query)
		
		query_response = cur.fetchall()
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	return query_response


if __name__ == '__main__':
    response = exec("SELECT version()")
    print(response)
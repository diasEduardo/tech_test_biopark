import psycopg2
import sys
sys.path.append('../utils')
from config_parser import config



def exec(query):
	conn = None
	query_response = None
	try:
		params = config("db.ini","postgresql")
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
    response = exec("SELECT * from send_type")
    print(response)
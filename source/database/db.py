import sys
sys.path.append('../utils')
import psycopg2
from psycopg2.extras import RealDictCursor
from config_parser import config
import json
from datetime import datetime

params = config("C:\\Users\\Eduardo\\Documents\\git_projects\\tech_test_biopark\\source\\database\\db.ini","postgresql")

def dt_parser(dt):
    if isinstance(dt, datetime):
        return dt.isoformat()

def exec(query):
	conn = None
	query_response = None
	try:
		
		conn = psycopg2.connect(**params)
		
		cur = conn.cursor(cursor_factory=RealDictCursor)
		cur.execute(query)
		
		query_response = json.dumps(cur.fetchall(), indent=2,default=dt_parser)
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	return query_response

def delete(query):
	conn = None
	query_response = None
	try:
		
		conn = psycopg2.connect(**params)
		
		cur = conn.cursor(cursor_factory=RealDictCursor)
		cur.execute(query)
		query_response = cur.rowcount;
		conn.commit();
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	return query_response


if __name__ == '__main__':
	query = "DELETE FROM send_schedule "\
			"WHERE id = 7" 
	response = delete(query)
	print(response)
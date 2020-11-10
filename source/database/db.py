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


if __name__ == '__main__':
	query = "SELECT s.id, st.status, t.type, r.name, r.email, r.phone, s.date_time, s.message "\
		"FROM send_schedule AS s "\
		"JOIN send_status AS st ON s.status_id = st.id "\
		"JOIN send_type AS t ON s.type_id = t.id "\
		"JOIN receiver AS r ON s.receiver_id = r.id "
	response = exec(query)
	print(response)
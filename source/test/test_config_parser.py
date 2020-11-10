import sys
sys.path.append('../utils')
from config_parser import config
import db

def test_config():
	assert config("../database/db.ini","postgresql") != "Section postgresql not found in the  ../database/deb.ini file"




test_config();
print("test_config pass")


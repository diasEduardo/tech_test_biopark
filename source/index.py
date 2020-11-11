from flask import Flask
import sys
sys.path.append('../api')
sys.path.append('api')
from api import api_app
import sys
sys.path.append('..')
app = Flask(__name__)

app.register_blueprint(api_app)


if __name__ == '__main__':
	app.run()
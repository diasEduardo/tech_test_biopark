from flask import Flask
import sys
sys.path.append('../api')
sys.path.append('api')
sys.path.append('../frontend')
sys.path.append('frontend')
sys.path.append('..')
from api import api_app
from frontend import frontend_app

app = Flask(__name__)

app.register_blueprint(api_app)
app.register_blueprint(frontend_app)


if __name__ == '__main__':
	app.run()
from flask import Blueprint


frontend_app = Blueprint('frontend_app', __name__)


@frontend_app.route('/', methods=['GET'])
def home_page():
	return "HOME PAGE HERE"
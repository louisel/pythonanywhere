from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
	return 'Website for testing how open graph tags work'

@app.route('/redirect302')
def redirect_302():
	response = redirect('redirect301')
	response.headers = _headers('302 redirect', 'redirect301', 'Redirects to /redirect301')
	return response

@app.route('/redirect301')
def redirect_301():
	response = redirect('ogurl')
	response.headers = _headers('301 redirect', 'ogurl', 'Redirects to /ogurl')
	return response

@app.route('/ogurl')
def ogurl():
	return 'redirect'

@app.route('/final')
def final():
	return 'redirect'

def _headers(title: str, relative_url: str, description: str):
	return {'og:title': title, 'og:type': 'website', 'og:url': 'http://louisel.pythonanywhere.com/' + url, 'og:image': 'http://louisel.pythonanywhere.com/ogp-icon.png', 'og:description': description}
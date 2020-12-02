from flask import Flask, render_template

def  create_app():
	app = Flask(__name__)

	@app.route('/')
	def hello_world():
	    return 'BEY, World!'

	@app.route('/hello/')
	@app.route('/hello/<name>')
	def hello(name=None):
	    return render_template('template.html', name=name)

	return app
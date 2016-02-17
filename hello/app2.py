from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = 'asdfg'
@app.route('/')
def hello():
	return "Hello world! Hi " + session.username

@app.route('/<name>/<int:answer>')
def guess(name, answer):
	correct = (answer == 42)
	return render_template(
		'guess.html',
		name=name,
		correct=correct,
	)

@app.route('/hello_login/', methods=['POST'])
def hello_login():
		session['username'] = request.form['username']
		return render_template(
			'login.html',
			username=request.form['username'],
			
		)
if __name__ == '__main__':
	app.run(debug=True)


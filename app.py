from flask import Flask, render_template, request
from database import add_participent_to_DB, load_participents

app = Flask(__name__)


@app.route('/')

# @app.route('/home')




@app.route('/join', methods=['GET', 'POST'])
def join():
	if request.method == 'POST':
		data = request.form
		add_participent_to_DB(data)
		return "Success"
	# 	# return render_template("index.html")
	# else:
	# 	return render_template('join.html')


@app.route('/participants')
def participants():
	data = load_participents()
	return data


if __name__ == '__main__':
	app.run(debug=False)

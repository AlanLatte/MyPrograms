<<<<<<< HEAD
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def main_template():
	return render_template('index.html')


if __name__ == '__main__':
=======
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def main_template():
	return render_template('index.html')


if __name__ == '__main__':
>>>>>>> Some error have exists
	app.run()
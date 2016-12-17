from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
	return 'Barackpore R.S Success Institute'

if __name__ == '__main__':
	app.run()
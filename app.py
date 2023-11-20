from flask import Flask, render_template, request 
import sqlite3 

app = Flask(__name__, template_folder='./')

@app.route('/') 
@app.route('/home') 
def index(): 
	return render_template('index.html') 

@app.route('/signup.html') 
def signup(): 
	return render_template('create.html') 


connect = sqlite3.connect('database.db') 
connect.execute( 
	'CREATE TABLE IF NOT EXISTS PARTICIPANTS (name TEXT,  email TEXT, password TEXT)') 


@app.route('/ruser.html', methods=['GET', 'POST'])
def ruser(): 
	if request.method == 'POST': 
		name = request.form['name'] 
		email = request.form['email'] 
		password = request.form['password'] 
	

		with sqlite3.connect("database.db") as users: 
			cursor = users.cursor() 
			cursor.execute("INSERT INTO PARTICIPANTS (name,email,password,) VALUES (?,?,?)", (name, email, password)) 
			users.commit() 
		return render_template("index.html") 
	else: 
		return render_template('create.html') 


@app.route('/participants') 
def participants(): 
	connect = sqlite3.connect('database.db') 
	cursor = connect.cursor() 
	cursor.execute('SELECT * FROM PARTICIPANTS') 

	data = cursor.fetchall() 
	return render_template("participants.html", data=data) 


if __name__ == '__main__': 
	app.run(debug=False) 

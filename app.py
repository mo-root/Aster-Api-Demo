from flask import Flask, request, redirect
import pyrebase

config = {
  "apiKey": "AIzaSyC6_SRpLMbZtV7I5ZT32w8vjDwXO-6wqs4",
  "authDomain": "aster4u-a47b9.firebaseapp.com",
  "databaseURL": "https://aster4u-a47b9-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "aster4u-a47b9",
  "storageBucket": "aster4u-a47b9.appspot.com",
  "messagingSenderId": "934119027505",
  "appId": "1:934119027505:web:e6376319c0a29a5fa0b610",
  "measurementId": "G-NTYT2E23LX"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()



app = Flask(__name__)
#Bootstrap(app)


app.config['SECRET_KEY'] = 'you-will-never-guess'




@app.route('/')
def fullList1():
    return 'Aster api'


@app.route('/<string:topic>')
def getS(topic):
    topic = db.child("Links").child(topic).get().val()
    return redirect(topic)


if __name__ == '__main__':
	app.run(debug=True)

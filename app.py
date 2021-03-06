from flask import Flask, render_template, request, redirect, url_for
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
    topic = db.child("Links").child(topic).child(topic).get().val()
    return redirect(topic)

#add a school to the database

@app.route('/School/<string:name>')
def addSchool(name):
    if(db.child("Schools").child(name).child("numbers").get().val() == None):
        db.child("Schools").child(name).child("numbers").set(1)
        return "Successfully Added"
    a = db.child("Schools").child(name).child("numbers").get().val()
    db.child("Schools").child(name).child("numbers").set(a+1)
    return "Successfully Added"


#adding a lookup search
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = "Can't enter"
    if request.method == 'POST':
        try:
            tropic = {
                request.form['Fname']: request.form['Lname']
                }
            db.child("Links").child(request.form['Fname']).set(tropic)

            return render_template('About.html')
        except:
            error = "topic already exists"
            return render_template('About.html', error=error)

    return render_template('About.html', error=error)





if __name__ == '__main__':
	app.run(debug=True)

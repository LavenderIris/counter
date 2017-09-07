from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)

app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

# routing rules and rest of server.py below


@app.route('/')
def index():
    if 'num' not in session:
        session['num']=random.randint(0,101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['num'])
    print "Guess:", guess, "session:", session['num']
    if 'message' in session:
        session.pop("message")
    if session['num']==guess:
        print "you win!"
        session['message']="You win"
    elif guess < session['num']:
        print "Your number is too low!"
        session['message']="Too low"
        
    elif guess > session['num']:
        print "Your number is too high"
        session['message']="Too high"
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    # clear all the values in my session key
    session.clear()
    return redirect('/')

app.run(debug=True) # run our server
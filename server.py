from flask import Flask, render_template, request, redirect, session
from time import gmtime, strftime
import random

app = Flask(__name__)

app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

# routing rules and rest of server.py below


@app.route('/')
def index():
    if "gold" not in session:
        session['gold']=0
    return render_template('index.html', gold=session['gold'])

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form["building"]
    
    print request.form
    # assume it's green, unless you lose money at the casino
    color='green'
    
    if (building=="farm"):
        # if it's a farm, earn 10-20 gold
        gold_earned = random.randint(10, 20)
    elif (building=="cave"):
    # if it's a cave, earn 10-20 gold
        gold_earned = random.randint(5, 10)
    elif (building=="house"):
    # if it's a cave, earn 2-5 gold
        gold_earned = random.randint(2, 5)
    elif (building=="casino"):
    # if it's a cave, earn 2-5 gold
        gold_earned = random.randint(-50, 50)
        if gold_earned<0:
            color='red'
    
    mytime=strftime("%Y/%m/%d %H:%M:%S", gmtime())

    if 'activity' not in session:
        session['activity']= [['Earned {} gold from the {}! ({})'.format(gold_earned, building, mytime), color ]]
    else:
        session['activity'].append(['Earned {} gold from the {}! ({})'.format(gold_earned, building, mytime), color])
    session['gold']+= gold_earned
    print "ACTIVITY", session['activity']
    print "GOLD ADDED", gold_earned
    
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True) # run our server
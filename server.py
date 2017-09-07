from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
app.count = 0
# routing rules and rest of server.py below


@app.route('/')
def index():
    # main page
    app.count+= 1
    session['count'] = app.count
   # redirects back to the '/' route
    return render_template('index.html')

@app.route('/addcount', methods=['POST'])
def add2count():
    # if a button is pressed, add +2
    app.count += 1 
    session['count'] = app.count
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    app.count=-1
    session['count']=app.count
    return redirect('/')

app.run(debug=True) # run our server
from flask import Flask,request,render_template

app=Flask(__name__)

# method 1
@app.route('/')
def index():
    return render_template('index.html')

# Method 2
def gfg():
   return 'geeksforgeeks'

app.add_url_rule('/gfg', 'g2g', gfg)

#dynamic url creation
# add variables in your web app

@app.route('/greet/<name>')
def greet(name):
    return "hi %s" % name 

#teling flask to accept post request from form/api
#using post method in route 
#/submit accept krega post value

@app.route('/login',methods=['POST'])
def login():
    if request.method=='POST':
        user = request.form['nm']  #form ne post bhji /submit pe
        #yha hmne store krlia user ko backend k liye

        return render_template('login.html',user=user)
    return render_template('index.html')

# user opens / → Flask sends index.html to the browser.

# User fills the form → browser sends POST request to /login.

# Flask receives the POST request → extracts user from the form.

# Flask renders login.html, injecting user dynamically → sends it back to browser.

# Browser displays HTML with the user’s name.

# main.................

if __name__=='__main__':

    app.run(debug=True)


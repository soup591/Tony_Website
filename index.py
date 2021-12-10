from flask import Flask, render_template, url_for, flash, redirect

"""
Set variable "app" to an instance of the Flask class.
__name__ is a special variable in Python that just means 
the name of the module. It can be equal to "__main__".
Basically, this is so Python knows where to look for your
templates, static files, etc. 
"""

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def home():
    return "Hello, user."

@app.route("/About/")
@app.route("/about")
def about():
    return "This will be where Tony's 'about' info will go."

@app.route("/Inquire/")
def inquire():
    return "This will be where an email / contact form is."

@app.route("/Deposit/")
def deposit():
    return "This will be where Tony can link his Venmo to take deposits."

@app.route("/Gallery/")
def gallery():
    return "This will host all of Tony's works in a visually appealing manner."


"""
We can use the below statement to run the debugger and dynamically update our
website without shutting it down and restarting every time changes are made.
"""
if __name__ == '__main__':
    app.run(debug=True)

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
    return render_template("home.html", page="home")

@app.route("/about")
def about():
    return render_template("about.html", page="about")

@app.route("/inquire/")
def inquire():
    return render_template("inquire.html", page="inquire")

@app.route("/deposit/")
def deposit():
    return render_template("deposit.html", page="deposit")

@app.route("/gallery/")
def gallery():
    return render_template("gallery.html", page="gallery")


"""
We can use the below statement to run the debugger and dynamically update our
website without shutting it down and restarting every time changes are made.
"""
if __name__ == '__main__':
    app.run(debug=True)

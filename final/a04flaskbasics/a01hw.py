from flask import Flask,redirect,url_for

app = Flask(__name__)
#Next we create an instance of this class. The first argument is
#  the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for 
# resources such as templates and static files.

@app.route("/<name>")
def user(name):
     return f"Hello  {name}!"

@app.route("/admin")
def admin():
     return redirect(url_for("home"))# observe home is a functionname
#have some logic thru which we can we can go to different places.


#not url name..




@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home")
def home():
       return "hello , this is main page"


app.debug=True

if __name__ == "__main__":
    app.run(debug=True)


# to run the application
#flask --app hello run




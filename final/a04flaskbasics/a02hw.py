from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)
#Next we create an instance of this class. The first argument is
#  the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for 
# resources such as templates and static files.

@app.route("/hp/<info>")
def htmlformakeup(info):#step 5
     return render_template("a01.html",msg=info)


@app.route("/horrible") #step6
def anotherhtmlformakeup():
     return render_template("a02.html")

@app.route("/freaky") #step 7
def whocaresforthisfunction():
     return render_template("a02.html",content=["A","B","C"])

@app.route("/<name>") #step 3
def user(name):
     return f"Hello  {name}!"

@app.route("/admin")  #step 4
def admin():
     return redirect(url_for("user",name="scrap"))# observe home is a functionname
#how to pass parameters to the URI.. 
#have some logic thru which we can we can go to different places.


#not url name..




@app.route("/")  #step 1
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home") #step2
def home():
       return "hello , this is main page"

app.debug=True

if __name__ == "__main__":
    app.run()


# to run the application
#flask --app hello run




from flask import Flask,redirect,url_for,request,session

app = Flask(__name__)

@app.route("/poc")
def home():
       return "the web app seems to be working"

@app.route("/login",methods=["POST","GET"])
def login():
    user=request.form["nm"] #read a parameter value,remember form is a dictionary..
    if request.method == "POST":
        return "post at work"
    elif request.method == "GET":
         return "get at work"

    return  "login at work"


@app.route("/<usr>",methods=["POST","GET"])
def login(usr):
    return  f"login at work {usr}"




if __name__ == "__main__":
    app.run(debug=True)
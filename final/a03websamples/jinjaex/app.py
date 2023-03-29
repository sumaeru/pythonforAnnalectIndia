from flask import Flask,render_template

app=Flask(__name__)

headings=("Name","Role","Salary1")

data=(
    ("A","role1","23"),
    ("B","role2","24"),
    ("C","role3","25"),
)


@app.route("/")
def display():
    return render_template("table.html",headings_hn=headings,data_hn=data)

app.run(debug=True)

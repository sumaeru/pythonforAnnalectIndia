from io import BytesIO
from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.utils import secure_filename
import os
from io import BytesIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///freak.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER







#how you store the files find out in your project
#dont waste your time doing google search...
#becuase storing file in db.. may cause entertainments..

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        upload = Upload(filename=file.filename, data=file.read())
        db.session.add(upload)
        db.session.commit()
        print("are we reaching here")
        data={"uploaded":file.filename}
        return data
    return {"upload" :"failed"}

@app.route('/download/<upload_id>')
def download(upload_id):
    upload = Upload.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.data), attachment_filename=upload.filename, as_attachment=True)


app.run(debug=True)

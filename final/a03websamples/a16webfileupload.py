import os
from flask import Flask,send_file,request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from io import BytesIO


app = Flask(__name__)
api = Api(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
      'sqlite:///'+ os.path.join(basedir,'freak.db')
db = SQLAlchemy(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class FileData(db.Model):
    __tablename__='horror'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)

#lines to create table in flask alchemy..
#with app.app_context():
 #   db.create_all()
class HelloWorld(Resource):#class which can be shared like a restful
    def post(self,idoffile=None):
        # read input from request
        #send output as a json string.
        file=request.files.get("filename")
        filename=secure_filename(file.filename)
        filedata = FileData(filename=file.filename, data=file.read())
        db.session.add(filedata)
        db.session.commit()
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return {"message":"file uploaded"}
             
    def get(self,idoffile=None):
        
        
        filetoclient = FileData.query.filter_by(id=idoffile).first()
        if filetoclient is not None:
            bytes=filetoclient.data
            return send_file(BytesIO(bytes),as_attachment=True,download_name=filetoclient.filename)
        else:
            return {'message':'no file found'}
        
        
    
  

 #register this as a resource.
api.add_resource(HelloWorld,"/pocreadandwritefile/<idoffile>","/pocreadandwritefile/")   













app.run(debug=True)




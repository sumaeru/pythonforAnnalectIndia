from flask import Flask,request,send_file
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from werkzeug.utils import secure_filename
import os
from io import BytesIO


app = Flask(__name__)
api = Api(app) # we are using restful api
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER










class HelloWorld(Resource):#class which can be shared like a restful
    def post(self,idoffile=None):
        # read input from request
        #send output as a json string.
        file=request.files.get("filename")
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return {"message":"file uploaded"}
        



        
    def get(self,idoffile=None):
        print("id of file ",idoffile)
        mtype="appliation/pdf"
        if idoffile=="1":# will be in hell if you dont know
            #how what data type we are getting
            filename=os.path.join(UPLOAD_FOLDER,'one.txt')
            mtype="text/plain"
        else:
            filename=os.path.join(UPLOAD_FOLDER,'names.pdf')  
        print(filename,"ok is this ")
        fileread=open(filename,"br")
        bytes=fileread.read()
        #return send_file(BytesIO(bytes),as_attachment=True,download_name="freak.txt",mimetype=mtype)
        return send_file(BytesIO(bytes),as_attachment=True,download_name=filename,mimetype=mtype)
        
    
  

 #register this as a resource.
api.add_resource(HelloWorld,"/pocreadandwritefile/<idoffile>")   
app.run(debug=True) #dont use in production envrionment





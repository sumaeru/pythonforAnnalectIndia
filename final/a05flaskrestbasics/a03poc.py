from flask import Flask,request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
api = Api(app) # we are using restful api


devices_args_parse = reqparse.RequestParser()
devices_args_parse.add_argument("name",type=str,help="device name has to given",required=True)
devices_args_parse.add_argument("status",type=bool,help="devicestatus")
 





class Device(Resource):#class which can be shared like a restful
    def get(self,device_id):
        if device_id==23:
            abort(404,message="invalid results")
        return {"msg":"get method at work"}
    def post(self,device_id):
        #return { "msg":request.form['key']}
        inputs=devices_args_parse.parse_args()
        return { "deviceinfo" : inputs},201 
    def delete(self,device_id):
        return { "msg":"delete at work"}
    def put(self,device_id):
        return { "msg":"put at work"}
  

 #register this as a resource.
api.add_resource(Device,"/device/<int:device_id>")   





app.run(debug=True) #dont use in production envrionment

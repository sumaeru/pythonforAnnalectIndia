from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
api = Api(app) # we are using restful api

class HelloWorld(Resource):#class which can be shared like a restful
    def get(self,someparam):
        return {"msg":someparam}
    def post(self):
        return { "msg" :"post at work"}
    def delete(self):
        return { "msg":"delete at work"}
    def put(self):
        return { "msg":"put at work"}
  

 #register this as a resource.
api.add_resource(HelloWorld,"/poc/<string:someparam>")   


app.run(debug=True) #dont use in production envrionment

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)



class ItemResource(Resource):
    def get(self):# plan to get items based on price
        
        return { "mode":"get"}
    def post(self):#plan to add items
        return { "modee":"post"}
    def delete(Self):#plan to remove item base on itemno
        return { "mode":"delete"}
    def put(self): #plan to update item 
        return { "mode":"put"}
    
    
api.add_resource(ItemResource,'/item/')

#observe above line we are telling for this URI.

app.run(debug=True)

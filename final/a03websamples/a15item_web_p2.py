#in this file all we are focussing on is
#how to get input, and how to show the output in correct json
#format..


from flask import Flask, request,json,jsonify
from flask_restful import Resource, Api,reqparse,fields,marshal_with
from a15item_db2 import Item,ItemStatus

#input needed for querying on price or category..
queryparameters=reqparse.RequestParser();
queryparameters.add_argument("itemprice",type=int,help="item price must bea number")
queryparameters.add_argument("categoryname",type=str,help="input argument must be string")
queryparameters.add_argument("itemno",type=int,help="itemno argumetn must be a number")

#input needed for adding and updating
addandupdate=reqparse.RequestParser();
addandupdate.add_argument("itemno",type=int,required=True,help="itemno is compulsory")
addandupdate.add_argument("itemname",type=str,required=True,help="itemname is compulsory")
addandupdate.add_argument("price",type=str,required=True,help="item price is compulsory")
addandupdate.add_argument("categoryname",type=str,help="item category name is compulsory")
#data has to come as json string in the body of the request


#input needed for deleting
deletearguments=reqparse.RequestParser();
deletearguments.add_argument("itemno",type=int,required=True,help="itemno is compulsory")


#for json reprsentation of Item class
item_fields = {
	'itemno': fields.Integer,
	'itemname': fields.String,
	'price': fields.Integer,
	'category': fields.String
}

#for json representation of ItemStatus class
item_status_fields={

    'status':fields.Integer,
    'message':fields.String,
    'itemobject':fields.Nested(item_fields)
}



app = Flask(__name__)
api = Api(app)

class ItemResource(Resource):
    

    #get funtion wil be used to get based on itemno..
    #or on price
    # or on category
    @marshal_with(item_fields) #this will ensure object gets converted
    #into a json string, including a list
    def get(self):
        inputgot=queryparameters.parse_args()
        if inputgot["itemprice"]:
            print("got itemprice")
        elif inputgot['categoryname']:
            print("got categoryname")
        elif inputgot['itemno']:
            print("got itemno")

        else:
            print("did not get anything")
        output=[Item(1,"X",3,"y")] #this is result of query    
        return output,200 #here observe empty list means no result got
    #filled up result indicatesresult got
    
    @marshal_with(item_status_fields)
    def post(self):#plan to add items
        input=addandupdate.parse_args();
        itemobject_foradding=Item(input['itemno'],input['itemname'],
                                  input['price'],input['categoryname'])
        output=ItemStatus(1,"hello",itemobject_foradding)
        if output.status==1:
            return output,201 #http status code 201 indicates created 
        else:
            return output,404
    @marshal_with(item_status_fields)
    def delete(Self):#plan to remove item base on itemno
        input=addandupdate.parse_args();
        itemno_tobedeleted=input['itemno']
        outputgivenbydeletelogic=ItemStatus(1,"hello",Item(1,"X",3,"Y"))
        if outputgivenbydeletelogic.status==1:
            return outputgivenbydeletelogic,200
        else:
            return outputgivenbydeletelogic,404
        return { "mode":"delete"}
    
    @marshal_with(item_status_fields)
    def put(self): #plan to update item 
        print("for updating")
        input=addandupdate.parse_args();
        input=Item(input['itemno'],input['itemname'],
                                  input['price'],input['categoryname'])
        output=ItemStatus(1,"hello",input)
        if output.status==1:
            return output,200
        else:
            return output,404
    
    
api.add_resource(ItemResource,'/item')



app.run(debug=True)

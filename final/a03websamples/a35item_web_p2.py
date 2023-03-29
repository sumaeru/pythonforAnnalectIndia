#in this file all we are focussing on is
#how to get input, and how to show the output in correct json
#format..

import json
from flask import Flask, request,json,jsonify
from flask_restful import fields,marshal_with,abort
from a15item_db2 import Item,ItemStatus


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


@app.errorhandler(400)
def not_found(error):
    return {'message':'did not get correct inputs'}, 400
    

    #get funtion wil be used to get based on itemno..
    #or on price
    # or on category

@app.route("/getItemDetails",methods=["GET"])
@marshal_with(item_fields) #this will ensure object gets converted
    #into a json string, including a list
def getItemDetailsBasedonQuery():
        inputgot=request.json()
        if inputgot["itemprice"]:
            print("got itemprice")
        elif inputgot['categoryname']:
            print("got categoryname")
        elif inputgot['itemno']:
            print("got itemno")
        else:
            return {'message':'no inputs where given'}
            
        output=[Item(1,"X",3,"y")] #this is result of query    
        return output,200 #here observe empty list means no result got
    #filled up result indicatesresult got

@app.route("/addItemDetails",methods=["POST"])    
@marshal_with(item_status_fields)
def addItem():#plan to add items
    output=ItemStatus(1,"failed adding",None)
    try:
        inputparams=request.json
        print(inputparams)
        itemobject_foradding=Item(inputparams['itemno'],inputparams['itemname'],
                                  inputparams['price'],inputparams['categoryname'])
        output.itemobject=itemobject_foradding
        output.status=1
        output.message='added'
        print("are we reaching here")
        if output.status==1:
            return output, 201 #http status code 201 indicates created 
        else:
            return output, 404
    except (KeyError,TypeError) as input_error:
         output.message="invalid content"
         return output,404

@app.route("/removeItemDetails",methods=["DELETE"])
@marshal_with(item_status_fields)
def delete():#plan to remove item base on itemno
    inputparams=request.json
    itemno_tobedeleted=inputparams['itemno']
    outputgivenbydeletelogic=ItemStatus(1,"hello",Item(1,"X",3,"Y"))
    if outputgivenbydeletelogic.status==1:
        return outputgivenbydeletelogic,200
    else:
        return outputgivenbydeletelogic,404
    
    
@app.route("/updateItemDetails",methods=["PUT"])
@marshal_with(item_status_fields)
def updateItem(): #plan to update item 
    print("for updating")
    inputparams=request.json
    print(inputparams)
    itemobject_foradding=Item(inputparams['itemno'],inputparams['itemname'],
                                  inputparams['price'],inputparams['categoryname'])
    output=ItemStatus(1,"hello",itemobject_foradding)
    if output.status==1:
        return output,200
    else:
        return output,404


app.run(debug=True)

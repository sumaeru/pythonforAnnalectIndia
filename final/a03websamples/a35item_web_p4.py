#in this file all we are focussing on is
#how to get input, and how to show the output in correct json
#format..

import json
from flask import Flask, request,json,jsonify
from flask_restful import fields,marshal_with,abort
from a15item_db3 import Item,ItemStatus,ItemDB


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

#itemDB object
itemDB=ItemDB()


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
        inputgot=request.json
        print(inputgot)
        if inputgot['price']:
             output=itemDB.find_items_less_than_price(inputgot['price'])
        elif inputgot['category']:
            output=itemDB.find_items_for_a_category(inputgot['category'])
        elif inputgot['itemno']:
             output=itemDB.find_item(inputgot['itemno'])
        else:
             pass
        return output,200
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
        output=itemDB.addItem(itemobject_foradding)
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
    outputgivenbydeletelogic=itemDB.deleteItem(itemno_tobedeleted)
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
    updatedobject=Item(inputparams['itemno'],inputparams['itemname'],
                                  inputparams['price'],inputparams['categoryname'])
    output=itemDB.updateItem(updatedobject)
    if output.status==1:
        return output,200
    else:
        return output,404
app.run(debug=True)

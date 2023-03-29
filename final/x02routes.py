from x01myapp import app
from flask import request,json,jsonify
from flask_restful import fields,marshal_with,abort
from x03model import Item,ItemStatus
from x05db import ItemDB
from flask_httpauth import HTTPBasicAuth
from flask_marshmallow import Marshmallow,fields


itemDB=ItemDB()

#def checkInsert():
 #   print("hello")
    #crete input
    #item.db
    
#checkInsert();


USER_INFO={ "user":"1234" } # so called userid, password
auth=HTTPBasicAuth() 

# #security, who are you.. and what we can access..

#logic we are checking what is userid and passowrd
@auth.verify_password
def verify(username,password):
     validuser=USER_INFO.get(username)==password
     return validuser
 

# # we can use marshmellow also, look at x06pushthisintoarch.py


 #for json reprsentation of Item class
item_fields = {
 	'itemno': fields.Integer,
 	'itemname': fields.String,
 	'price': fields.Integer,
 	'category': fields.String
 }

# #for json representation of ItemStatus class
item_status_fields={

     'status':fields.Integer,
     'message':fields.String,
     'itemobject':fields.Nested(item_fields)
}


#ma = Marshmallow(app)
# class ItemSchema(ma.Schema):
#     itemno= fields.String()
#     itemname = fields.Email()
#     price = fields.Int()
#     category=fields.String()  


# class ItemStatus(ma.Schema):
#     status = fields.Int()
#     message = fields.String()
#     itemobject = fields.Nested(ItemSchema)


#itemDB object
itemDB=ItemDB()


@app.route("/poconsecurity")
@auth.login_required #write this below .. 
def bsf():
    return { "test":"poc at work" }



@app.errorhandler(400)
def kid_found(error):
    return {'message':'did not get correct inputs'}, 400


    
#     #get funtion wil be used to get based on itemno..
#     #or on price
#     # or on category

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
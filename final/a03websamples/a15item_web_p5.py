#in this file all we are focussing on is
#how to get input, and how to show the output in correct json
#format..
import os
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
api = Api(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
      'sqlite:///'+ os.path.join(basedir,'freak.db')
db = SQLAlchemy(app)

#with app.app_context():
   # db.create_all()




class ItemStatus:
    def __init__(self,status_code,message,itemobject):
        self.status=status_code
        self.message=message
        self.itemobject=itemobject

class Item(db.Model):
    __tablename__= "item" # table name
    itemno=db.Column("ino",db.Integer,primary_key=True)
    itemname=db.Column("itemname",db.String)
    price=db.Column("price",db.Integer)
    category=db.Column("category",db.String)

    def __init__(self,itemno,itemname,price,category):
        self.itemname=itemname
        self.itemno=itemno
        self.price=price
        self.category=category

    def __repr__(self):
        return f"{self.itemno} -- {self.itemname}  -- {self.price} --{self.category}"


#input needed for querying on price or category..
queryparameters=reqparse.RequestParser();
queryparameters.add_argument("price",type=int,help="item price must bea number")
queryparameters.add_argument("category",type=str,help="input argument must be string")
queryparameters.add_argument("itemno",type=int,help="itemno argumetn must be a number")

#input needed for adding and updating
addandupdate=reqparse.RequestParser();
addandupdate.add_argument("itemno",type=int,required=True,help="itemno is compulsory")
addandupdate.add_argument("itemname",type=str,required=True,help="itemname is compulsory")
addandupdate.add_argument("price",type=str,required=True,help="item price is compulsory")
addandupdate.add_argument("category",type=str,help="item category name is compulsory")
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




class ItemResource(Resource):
    

    #get funtion wil be used to get based on itemno..
    #or on price
    # or on category
    @marshal_with(item_fields) #this will ensure object gets converted
    #into a json string, including a list
    def get(self):
        output=[]
        inputgot=queryparameters.parse_args()
        if inputgot["price"]:
            output=Item.query.filter(Item.price < inputgot['price']) .all()
        elif inputgot['category']:
            output=Item.query.filter(Item.category ==inputgot['category']).all()
        elif inputgot['itemno']:
            item=Item.query.filter(Item.itemno ==inputgot['itemno']).first()
        else:
            abort(406,message="price or itemno or category needed")
        return output,200 #here observe empty list means no result got
    #filled up result indicatesresult got
    
    @marshal_with(item_status_fields)
    def post(self):#plan to add items
        input=addandupdate.parse_args();
        item=Item(input['itemno'],input['itemname'],
                                  input['price'],input['category'])
        itemstatus=ItemStatus(0,"add failed",None)
        try:
            db.session.add(item)
            db.session.commit()
            itemstatus.status=1
            itemstatus.message="added successfully"
            itemstatus.itemobject=item
        except:#when same id is added again
                itemstatus.message="Integrity error"
                db.session.rollback()
        if itemstatus.status==1:
            return itemstatus,201 #http status code 201 indicates created 
        else:
            return itemstatus,404
        


    @marshal_with(item_status_fields)
    def delete(Self):#plan to remove item base on itemno
        input=deletearguments.parse_args();
        itemno_tobedeleted=input['itemno']
        itemstatus=ItemStatus(0,"delete failed",None)
        dbobject =Item.query.filter_by(itemno=itemno_tobedeleted).first()
        if dbobject is not None:
            db.session.delete(dbobject)
            db.session.commit()
            itemstatus.status=1
            itemstatus.message="deleted successfully"
            itemstatus.itemobject=dbobject # this object is deleted.. from db
        
        if itemstatus.status==1:
            return itemstatus,200
        else:
            return itemstatus,404
        
    @marshal_with(item_status_fields) 
    def put(self): #plan to update item 
        print("for updating")
        input=addandupdate.parse_args();
        updatedobject=Item(input['itemno'],input['itemname'],
                                  input['price'],input['category'])
        itemstatus=ItemStatus(0,"update failed",None)
        dbobject =Item.query.filter_by(itemno=input['itemno']).first()
        if dbobject is not None:
            dbobject.itemname=updatedobject.itemname
            dbobject.price=updatedobject.price
            dbobject.category=updatedobject.category
            db.session.commit();
            itemstatus.status=1
            itemstatus.message="updated successfully"
            itemstatus.itemobject=updatedobject
        if itemstatus.status==1:
            return itemstatus,200
        else:
            return itemstatus,404
        
    
api.add_resource(ItemResource,'/item')



app.run(debug=True)

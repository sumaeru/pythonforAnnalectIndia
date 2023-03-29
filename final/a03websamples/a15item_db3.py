#started adding the sqlalchemy code..

from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import  sqlite
from sqlalchemy.exc import IntegrityError

Base =declarative_base()

class ItemStatus:#any class object which is not related to the database
    #dont make it as subclass of Base
    def __init__(self,status_code,message,itemobject):
        self.status=status_code
        self.message=message
        self.itemobject=itemobject

class Item(Base):
    __tablename__= "item" # table name
    itemno=Column("ino",Integer,primary_key=True)
    itemname=Column("itemname",String)
    price=Column("price",Integer)
    category=Column("category",String)

    def __init__(self,itemno,itemname,price,category):
        self.itemname=itemname
        self.itemno=itemno
        self.price=price
        self.category=category

    def __repr__(self):
        return f"{self.itemno} -- {self.itemname}  -- {self.price} --{self.category}"
        
class ItemDB():

    def __init__(self):
        engine =create_engine("sqlite:///freak.db",echo=True)
        #Base.metadata.create_all(bind=engine)
        Session=sessionmaker(bind=engine)#create the class
        self.session=Session()#object creation
        print("session created")
        #check after running this whether table is created or not.
    
    def addItem(self,item):
        itemstatus=ItemStatus(0,"add failed",None)
        try:
            self.session.add(item)
            self.session.commit()
            itemstatus.status=1
            itemstatus.message="added successfully"
            itemstatus.itemobject=item
        except IntegrityError:#when same id is added again
            itemstatus.message="Integrity error"
            self.session.rollback()
        return itemstatus
    
    def updateItem(self,item):
        itemstatus=ItemStatus(0,"update failed",None)
        dbobject =self.session.query(Item).filter_by(itemno=item.itemno).first()
        if dbobject is not None:
            dbobject.itemname=item.itemname
            dbobject.price=item.price
            dbobject.category=item.category
            self.session.commit()
            itemstatus.status=1
            itemstatus.message="updated successfully"
            itemstatus.itemobject=item
        return itemstatus
    

    def deleteItem(self,itemnogiven):
        itemstatus=ItemStatus(0,"delete failed",None)
        dbobject =self.session.query(Item).filter_by(itemno=itemnogiven).first()
        if dbobject is not None:
            self.session.delete(dbobject)
            self.session.commit()
            itemstatus.status=1
            itemstatus.message="deleted successfully"
            itemstatus.itemobject=dbobject # this object is deleted.. from db
        return itemstatus    
    
    def find_items_less_than_price(self,pricegiven):
        items=self.session.query(Item).filter(Item.price <pricegiven ).all()
        return items #check the length of items to know whether
    
    def find_items_for_a_category(self,categorygiven):
        items=self.session.query(Item).filter(Item.category ==categorygiven ).all()
        return items #check the length of items to know whether

    def find_item(self,itemno):
        items=[]
        item=self.session.query(Item).filter(Item.itemno ==itemno ).first()
        if(item):
            items.append(item)
        return items
    
    #end of the class DB

#check 1 is the object is getting created.
def check1():
    item=Item(1,"pencil",3,"stationery")
    print(item)




#check 2 checking adding of item is working or not
def checkAddingofItem():
    itemDB=ItemDB()
    item=Item(15,"A",3,"stn")
    itemstatus=itemDB.addItem(item)
    print(itemstatus.status,itemstatus.message)

#check 3 working on update item
def testupdateItem():
    itemDB=ItemDB()
    item=Item(15,"horrible",3,"junk")
    itemstatus=itemDB.updateItem(item)
    print(itemstatus.status,itemstatus.message)

#check 4 deleted item
def checkitemdelete():
    itemDB=ItemDB()
    itemstatus=itemDB.deleteItem(14)
    print(itemstatus.status,itemstatus.message)

#check 5, find items less than the price.
def checkItemslessthantheprice():    
    itemDB=ItemDB()
    pricegiven=100
    items=itemDB.find_items_less_than_price(pricegiven)
    for item in items:
        print(item)
    print(len(items),"is this the length")

#check 6 find all items which belong to a category
#items found less than the price or not
def checkforCategory():
    categorygiven="stn"
    itemDB=ItemDB()
    items=itemDB.find_items_for_a_category(categorygiven)
    print(len(items),"ok database layer is over")
    #know here each element in the list is an item, use type.. command
    #to find out if you have any.

#check 7 -- idea is to have a list returned in all queries.
#list is empty mean itemno is not found 
def checkItem():
    itemno=100
    itemDB=ItemDB()
    itemstatus=itemDB.find_item(itemno)
    print(len(itemstatus))


#checkItemslessthantheprice() 



    




    

    
    



















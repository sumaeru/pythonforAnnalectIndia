#started adding the sqlalchemy code..

from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import  sqlite
from sqlalchemy.exc import IntegrityError


Base =declarative_base()

class ItemStatus:
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
        

engine =create_engine("sqlite:///freak.db",echo=True)
#Base.metadata.create_all(bind=engine)
Session=sessionmaker(bind=engine)#create the class
session=Session()#object creation
print("session created")
#check after running this whether table is created or not.





#check 1 is the object is getting created.
def check1():
    item=Item(1,"pencil",3,"stationery")
    print(item)

#check 2 wrote add item logic
def addItem(item):
    itemstatus=ItemStatus(0,"add failed",None)
    try:
        session.add(item)
        session.commit()
        itemstatus.status=1
        itemstatus.message="added successfully"
        itemstatus.itemobject=item
    except IntegrityError:#when same id is added again
        itemstatus.message="Integrity error"
        session.rollback()
    return itemstatus


#checking adding of item is working or not
def checkAddingofItem():
    item=Item(15,"A",3,"stn")
    itemstatus=addItem(item)
    print(itemstatus.status,itemstatus.message)

#check 3 working on update item
def updateItem(item):
    itemstatus=ItemStatus(0,"update failed",None)
    dbobject =session.query(Item).filter_by(itemno=item.itemno).first()
    if dbobject is not None:
        dbobject.itemname=item.itemname
        dbobject.price=item.price
        dbobject.category=item.category
        session.commit()
        itemstatus.status=1
        itemstatus.message="updated successfully"
        itemstatus.itemobject=item
    return itemstatus    


def testupdateItem():
    item=Item(15,"horrible",3,"junk")
    itemstatus=updateItem(item)
    print(itemstatus.status,itemstatus.message)

#check 4 deleted item
def deleteItem(itemnogiven):
    itemstatus=ItemStatus(0,"delete failed",None)
    dbobject =session.query(Item).filter_by(itemno=itemnogiven).first()
    if dbobject is not None:
        session.delete(dbobject)
        session.commit()
        itemstatus.status=1
        itemstatus.message="deleted successfully"
        itemstatus.itemobject=dbobject # this object is deleted.. from db
        
    return itemstatus    


def checkitemdelete():
    itemstatus=deleteItem(14)
    print(itemstatus.status,itemstatus.message)

#check 5, find items less than the price.
def find_items_less_than_price(pricegiven):
    items=session.query(Item).filter(Item.price <pricegiven ).all()
    return items #check the length of items to know whether
#items found less than the price or not


def checkItemslessthantheprice():    
    pricegiven=100
    items=find_items_less_than_price(pricegiven)
    for item in items:
        print(item)
    print(len(items),"is this the length")

#check 6 find all items which belong to a category
def find_items_for_a_category(categorygiven):
    items=session.query(Item).filter(Item.category ==categorygiven ).all()
    return items #check the length of items to know whether
#items found less than the price or not

def checkforCategory():
    categorygiven="stn"
    items=find_items_for_a_category(categorygiven)
    print(len(items),"ok database layer is over")
    #know here each element in the list is an item, use type.. command
    #to find out if you have any.

#end of writing databse.. i went from check to check 6.
#model was identified.. 

#check 7 -- idea is to have a list returned in all queries.
#list is empty mean itemno is not found 
def find_item(itemno):
    items=[]
    item=session.query(Item).filter(Item.itemno ==itemno ).first()
    if(item):
        items.append(item)
    return items

def checkItem():
    itemno=100
    itemstatus=find_item(itemno)
    print(len(itemstatus))

#checkItem()




    




    

    
    



















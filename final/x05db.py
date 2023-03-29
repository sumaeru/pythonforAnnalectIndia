from x03model import Item,ItemStatus
from sqlalchemy.exc import IntegrityError
from x01myapp import db

class ItemDB():
    def addItem(self,item):
        itemstatus=ItemStatus(0,"add failed",None)
        try:
            db.session.add(item)
            db.session.commit()
            itemstatus.status=1
            itemstatus.message="added successfully"
            itemstatus.itemobject=item
        except IntegrityError:#when same id is added again
            itemstatus.message="Integrity error"
            db.session.rollback()
        return itemstatus
    
    def updateItem(self,item):
        itemstatus=ItemStatus(0,"update failed",None)
        dbobject =Item.query.filter_by(itemno=item.itemno).first()
        if dbobject is not None:
            dbobject.itemname=item.itemname
            dbobject.price=item.price
            dbobject.category=item.category
            db.session.commit()
            itemstatus.status=1
            itemstatus.message="updated successfully"
            itemstatus.itemobject=item
        return itemstatus
    

    def deleteItem(self,itemnogiven):
        itemstatus=ItemStatus(0,"delete failed",None)
        dbobject =Item.query.filter_by(itemno=itemnogiven).first()
        if dbobject is not None:
            db.session.delete(dbobject)
            db.session.commit()
            itemstatus.status=1
            itemstatus.message="deleted successfully"
            itemstatus.itemobject=dbobject # this object is deleted.. from db
        return itemstatus    
    
    def find_items_less_than_price(self,pricegiven):
        items=Item.query.filter(Item.price < pricegiven).all()
        return items #check the length of items to know whether
    
    def find_items_for_a_category(self,categorygiven):
        items=Item.query.filter(Item.category ==categorygiven).all()
        return items #check the length of items to know whether

    def find_item(self,itemno):
        items=[]
        item=Item.query.filter(Item.itemno==itemno).first()
        if(item):
            items.append(item)
        return items
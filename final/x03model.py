from x01myapp import db

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






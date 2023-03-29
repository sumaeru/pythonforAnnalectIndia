
#how do we deal with failure and think only of success
#in functon design have already particpating ina  funeral.




class ItemStatus:
    def __init__(self,status_code,message,itemobject):
        self.status=status_code
        self.message=message
        self.itemobject=itemobject

class Item():
    
    

    def __init__(self,itemno,itemname,price,category):
        self.itemname=itemname
        self.itemno=itemno
        self.price=price
        self.category=category

    def __repr__(self):
        return f"{self.itemno} -- {self.itemname}  -- {self.price} --{self.category}"
        






#check 1 is the object is getting created.
def check1():
    item=Item(1,"pencil",3,"stationery")
    print(item)

#check 2 wrote add item logic
def addItem(item):  
    #decide on input and output and think how do you tell failure
    itemstatus=ItemStatus(0,"add failed",None)
    return itemstatus


#checking adding of item is working or not
def checkAddingofItem():
    item=Item(15,"A",3,"stn")
    itemstatus=addItem(item)
    print(itemstatus.status,itemstatus.message)

#check 3 working on update item
def updateItem(item):
    itemstatus=ItemStatus(0,"update failed",None)
    return itemstatus    


def testupdateItem():
    item=Item(15,"horrible",3,"junk")
    itemstatus=updateItem(item)
    print(itemstatus.status,itemstatus.message)

#check 4 deleted item
def deleteItem(itemnogiven):
    itemstatus=ItemStatus(0,"delete failed",None)
    return itemstatus    


def checkitemdelete():
    itemstatus=deleteItem(14)
    print(itemstatus.status,itemstatus.message)

#check 5, find items less than the price.
def find_items_less_than_price(pricegiven):
    items=[Item(1,"pencil",3,"school")] #deciding return type will
    # be a list and what it means from project point of view
    return items #check the length of items to know whether



def checkItemslessthantheprice():    
    pricegiven=100
    items=find_items_less_than_price(pricegiven)
    for item in items:
        print(item)
    print(len(items),"is this the length")

#check 6 find all items which belong to a category
def find_items_for_a_category(categorygiven):
    items=[Item(1,"pencil",3,"school")] #deciding return type will
    # be a list and what it means from project point of view
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
    return items # be clear about input and return type from the function

def checkItem():
    itemno=100
    itemstatus=find_item(itemno)
    print(len(itemstatus))






    




    

    
    



















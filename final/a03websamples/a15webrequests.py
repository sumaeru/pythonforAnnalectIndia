#read official docs
#https://requests.readthedocs.io/en/latest/user/quickstart/
import requests

#add image part and validation part..


URL="http://127.0.0.1:5000/item"

def calladdItem():
    dataforservice={"itemno":34, "itemname":'pencil',"price":44,"category":'abc'}
    response=requests.post(URL,json=dataforservice)
    print(response,response.json())# i hundred percent
    #knew response wes in json foramt... do you agre.





def callupdateItem():
    dataforservice={"itemno":34, "itemname":'eraser',"price":44,"category":'freak'}
    response=requests.put(URL,json=dataforservice)
    print(response,response.json())



def callremoveItem():
    dataforservice={"itemno":34}
    response=requests.delete(URL,json=dataforservice)
    print(response,response.json())

#callremoveItem()


def getAllItemsOnPrice():
    dataforservice={"price":44}
    response=requests.get(URL,json=dataforservice)
    print(response,response.json())

#getAllItemsOnPrice()
                    
    

def getIndividualItem():
    dataforservice={"itemno":13}
    response=requests.get(URL,json=dataforservice)
    print(response,response.json())

#getIndividualItem()

def getItemsBasedonCategory():
    dataforservice={"category":'category'}
    response=requests.get(URL,json=dataforservice,timeout=3)
    #use passing form parameters
    #requests.post('https://httpbin.org/post', data={'key': 'value'})

    #use passing query parameters
    #payload = {'key1': 'value1', 'key2': 'value2'}
    #r = requests.get('https://httpbin.org/get', params=payload)

    #after 3 seconds dont wait for response show it has failure
    print(response,response.json())

getItemsBasedonCategory();
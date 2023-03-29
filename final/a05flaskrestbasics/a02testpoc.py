import requests

BASE="http://127.0.0.1:5000/"


def getcall():
    response= requests.get(BASE + "poc/junk") #change it get, post, put , delete
    print(response.json())


def postcall():
    response = requests.post(BASE+"device/3",{"name":"pressuresensor","status":True})
    print(response.json())


def anothergetcall():
    response=requests.get(BASE+"device/23")    
    print(response.json())
    #if you dont have json as a database ..use response..

    



#postcall();
anothergetcall();









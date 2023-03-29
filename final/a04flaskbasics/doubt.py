from flask import Flask,request,json
from device import Device

app = Flask(__name__) #creation of the flask object

@app.route("/il",methods=['POST'])
def takeInputViaBody():
      #here call the logic.py function pass json object
      #get a dictonary whichcontains real perimeter and area.
      #this will be the response.
      print(request.data,"hello this is ok")
      print(request.json,"freaky thing") #convert string into a json object
      data=request.json
      print(data['length'])
      return "freak"  
    



#request processing functions, shoud be written before server is started
@app.route("/admin",methods=['POST','GET'])
def scrapFunction(): #for function f1 to get called ...event has to occur
    scrap=request.form['junk']
    print("what we do python or flask does not care it is our logic")
    return "hi" # if we are returning some html page,, web for presentation
#web for service.


@app.route("/gl")
def listr():
    num=[1,2,3]
    return num

@app.route("/or")
def reo():
    d=Device(2,3);
    return json.dumps(d.__dict__)




#dont byheart this code.. 
if __name__ == "__main__":
    app.run(debug=True)

  #registering for the event, if the URI is admin
#mode of request is get then call this function.. 
#event handling function, it will  get called only when the event occurs.




import json

class Device:
    def __init__(self,deviceid,status):
        self.deviceid=deviceid
        self.status=status
    
x=Device(2,3)
y=Device(4,5)
print(x.deviceid)
print(json.dumps(x.__dict__))
listofdevices=[x,y]
jsonlist=json.dumps([x.__dict__ for x in listofdevices])
print(jsonlist,"ok see this output")






    

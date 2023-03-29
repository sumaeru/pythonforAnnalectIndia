#ensure you read the quick start of
#https://requests.readthedocs.io/en/latest/user/quickstart/

#run the program called a16webfileupload.py
#catch ConnectionError in case of problems
import requests

URL="http://127.0.0.1:5000/pocreadandwritefile/"

def fileupload():
    filedata={'filename': open("read.txt",'rb')}
    response = requests.post(URL,files=filedata)
    print(response,response.json())#status_code property will give you http status

def filedownload():
    id=3
    urlforquery=f"{URL}{id}"# get the URL right if you make a mess
    #horrible problem
    print(urlforquery)
    response = requests.get(urlforquery)
    print(response.status_code,response,response.content)
   # content is used for reading binary code






filedownload()


import os
from io import BytesIO
from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR,BINARY,LargeBinary
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import  sqlite
from sqlalchemy.exc import IntegrityError

#text file reading
def readingtextfile():
    file="poc.txt"
    fileread=open(file,"r")
    lines=fileread.read()
    print(lines,end='\n')





#binary file reading
def readingbinaryfile():
    file="a02killer.pdf"
    fileread=open(file,"br")
    bytes=fileread.read()
    print(bytes)# those who pritning the binary deserve nobel prize



Base =declarative_base()
# thinking of sqlalchemy model.
class ModelwithFile(Base):
    __tablename__='twf'
    id = Column(Integer, primary_key=True)
    filename = Column(String(50))
    data = Column(LargeBinary)# theory part in sql alchemy

    def __init__(self,id,filename,data):
        self.id=id
        self.filename=filename
        self.data=data

#lots of creativity can be shown..in how to get a session
#adapt according to the project..
def writetoFileAndReadFromFile():
    engine =create_engine("sqlite:///freak.db")
    #Base.metadata.create_all(bind=engine) #creating databases
    Session=sessionmaker(bind=engine)#create the class
    session=Session()
    file="a08csp.png"
    fileread=open(file,"br") #be conscious about what is file binary or text
    filecontent=fileread.read()
    modelwithfile=ModelwithFile(20,file,filecontent)

    session.add(modelwithfile)
    session.commit()
    print("hey")

    #read from db.
    #param=3
    #x=session.query(ModelwithFile).filter_by(id = param).first()
    
    #if x is not None:
     #   print("contents are coming hopefully",x.data)
    #else:
     #   print("query is not coming")













writetoFileAndReadFromFile()




















    
    



    
    



    


        




    





















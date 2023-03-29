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
    lines=fileread.readlines()
    print(lines,end='\n')

#binary file reading
def readingbinaryfile():
    file="a02killer.pdf"
    fileread=open(file,"br")
    bytes=fileread.read()
    print(bytes)
    fileread.close();


Base =declarative_base()
# thinking of sqlalchemy model.
class ModelwithFile(Base):
    __tablename__='twf'
    id = Column(Integer, primary_key=True)
    filename = Column(String(50))
    data = Column(LargeBinary)

    def __init__(self,id,filename,data):
        self.id=id
        self.filename=filename
        self.data=data

def start():
    engine =create_engine("sqlite:///freak.db",echo=True)
    Base.metadata.create_all(bind=engine)
    Session=sessionmaker(bind=engine)#create the class
    session=Session()#object creation
    print("hey")

start()
    
    



    
    



    


        




    





















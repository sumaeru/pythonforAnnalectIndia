#pip install sqlalchemy




from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import  sqlite

Base =declarative_base()

class Person(Base):
    __tablename__= "people" # table name
    ssn=Column("ssn",Integer,primary_key=True)
    firstname=Column("firstname",String)
    lastname=Column("lastname",String)
    gender=Column("gender",CHAR)
    age=Column("age",Integer)

    def __init__(self,ssn,firstname,lastname,gender,age): 
        self.ssn=ssn
        self.firstname=firstname
        self.lastname=lastname
        self.gender=gender
        self.age=age

    def __repr__(self):
        return f"{self.ssn} --{self.firstname} --{self.lastname}--{self.gender}--{self.age}"
    
class Thing(Base):
    __tablename__="things"
    tid=Column("tid",Integer,primary_key=True)
    description=Column("description",String)
    owner=Column("ssn",Integer,ForeignKey(Person.ssn))

    def __init__(self,tid,description,owner):
        self.tid=tid
        self.description=description
        self.owner=owner

    def __repr__(self):
        return f"{self.tid}  --{self.description} -- {self.owner}"

        
        
    




def poc():
 
    engine =create_engine("sqlite:///freak.db",echo=True)#rituals
    Base.metadata.create_all(bind=engine)#create tables
    Session=sessionmaker(bind=engine)#create the class
    session=Session()#object creation
    #person=Person(1,"A","B","m",35)
    #session.add(person)
    #session.commit();
    
    #results =session.query(Person).all()
    
    #results =session.query(Person).filter(Person.age < 60)
    #for r in results:
       # print(r)


   
    # t1=Thing(1,"pencil",2)
    # t2=Thing(2,"eraser",2)    
    # session.add(t1)
    # session.add(t2)
    # session.commit() 


    results = session.query(Thing,Person).filter(Thing.owner ==Person.ssn)
    for r in results:
        print(r)





    

poc()



     
       













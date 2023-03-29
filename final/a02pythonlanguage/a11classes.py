class Person:
  def __init__(self, name, age):
    self.name=name
    self.age=age


  def myfunc(self): # memeber function..
    print("Hello my name is " + self.name) 

p1 = Person("John", 36)
p1.myfunc()
p2=Person("ABC".44)
p2.myfunc();





class SavingAccount:
    def __init__(self, amount):
        # making the 'amount' variable private
        self.__amount = amount

    # method to display the amount
    def getAmount(self):
        print("Current amount -> ", self.__amount)

user = SavingAccount('10,000')
user.getAmount()
print(user.__amount)
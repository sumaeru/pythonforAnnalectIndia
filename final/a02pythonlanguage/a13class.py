class Customer:#creating a data type
    customerId=1
    name="hello"
    location="blr"
    mobile=23

    def getCustomerDetails():# operation 
        return customerId

#customer data type is there but no varible of customer has 
#been created by us
c1=Customer()  # c1=3
c1.customerId=4
c2=Customer() # c2=4     
c2.customerId=5
z=c1.getCustomerDetails()
print(z)
z=c2.getCustomerDetails()
print(z)

print("hi")



def subtract(x,y):#this function takes care of logic
    result=x-y
    return result


def startTheApp():#this funtion takes care of presentation
    
    x=float(input("enter first operand:"))
    y=float(input("enter second operand"))
    z=subtract(x,y)
    print("result is",z)
    


startTheApp();
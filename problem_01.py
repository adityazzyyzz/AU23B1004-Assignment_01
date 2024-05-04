#1
def get_name(a=input("enter your name :",)):
    
    return a

def get_tshirt(b):
    c=get_name()
    c=c.capitalize()
    f=["PUMA ", "NIKE", "HRX", "ADIDAS"]
    
    if b in f:
        print("hey",c,"the brand u are looking for is available : ")
    else:
        print("hey",c,"unfortumately the branfd you are looking for is not available right now ")    

d=input("enter the brand name you are looking for : ")
d=d.upper()
get_tshirt(d)
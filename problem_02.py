#2
def get_name(a=input("enter your name")):
    
    return a

def get_tshirt(b,x):
    c=get_name()
    c=c.capitalize()

    f=["puma ", "nike", "HRX", "adidas"]
    if b in f and len(x)==0:
        print("hey",c,"the brand u are looking for is available ")
    if b in f and len(x!=0):
        print("hey",c,"the brand u are looking for SIZE ",x," is available ")
    else:
        print("hey",c,"unfortumately the branfd you are looking for is not available right now ")

    
    
d=input("enter the brand name you are looking for")
e=input("enter the size (optional)")
d=d.upper
get_tshirt(d,e)

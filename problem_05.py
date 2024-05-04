def call():
    x = 2
    x = 5 - x / 2
    print(x)
def caller():
    x = 1
    while x < 20:
        print("x = " + str(x))
        call()  
        x *= 2
    print("x = " + str(x))
print(caller())
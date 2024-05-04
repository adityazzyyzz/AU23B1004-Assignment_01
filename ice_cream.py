
#4
#ice_cream.py
def add_topping(scoop_size, *toppings):#here the function is defined for the scoopsize and toppiings
    if scoop_size>1:# this if condition is for if the number of scoop is more than 1 then scoop should be plural
        print("adding",toppings," toppings to ",scoop_size,"scoops of ice cream.")
    else:#this else condition is for if the number of scoop is not more than 1 then scoop should be singular
        print("adding",toppings," toppings to ",scoop_size,"scoop of ice cream.")
def make_shake(type_of_shake):#this is another function which is defined for the type of shake you want to be made 
    print(type_of_shake," shake is being prepared.") 

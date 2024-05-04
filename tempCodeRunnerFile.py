#4
#making_icecream.py

#demonstration of full module 
import ice_cream#this import statement imports the ice_cream module which will help in using the functions in the module within this module  
print("Your order id being prepared with ")
ice_cream.add_topping(4, "tootyfrooty" ," chocochips ")#this statements gives the parameters to the add_toppings function made in ice_cream module
ice_cream.make_shake("chocolate")# this statements gives the parameters to the make_shake function made in ice_cream module 

#demonstration of specific function of add_toppings
ice_cream.add_topping(1,"sprinkles", "hot fudge") #this statements gives the parameters to the add_toppings function made in ice_cream module#4
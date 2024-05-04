AS = int(input("Annual Site Profit: "))
visitors_purchased = int(input("Number of Visitors Who Purchased: "))
site_visitors = int(input("Total Number of Site Visitors: "))
IMPROVED_visitors_purchased = int(input("IMPROVED Number of Visitors Who Purchased: "))
IMPROVED_site_visitors = int(input("IMPROVED Total Number of Site Visitors: "))
try:
    ICR = IMPROVED_visitors_purchased/IMPROVED_site_visitors
    CCR=visitors_purchased/site_visitors
except ZeroDivisionError as e:
    print("division by zero is not allowed",e)


if ICR>1 or CCR>1:
    raise Exception ("invalid conversion rate" )
else:
    pass
IMC = int(input("Improvement Cost: "))
EPL = int(input("Expected Project Life: "))
i = 0.05
ICR = IMPROVED_visitors_purchased/IMPROVED_site_visitors
CCR=visitors_purchased/site_visitors
if ICR>1 or CCR>1:
    raise Exception ("invalid conversion rate" )
else:
    pass

def future_gain():
    return (AS * (ICR / CCR) - AS) * ((1 + i) ** EPL - 1) / i - IMC * (1 + i) ** EPL

def total_gain():
    return future_gain() / (i + 1) ** EPL

def annual_gain():
    return total_gain() / EPL

def annual_roi():
    return annual_gain() / IMC

def total_roi():
    return total_gain() / IMC

print("future gain :",future_gain())
print("total gain :",total_gain())
print("annual gain :",annual_gain())
print("annual roi :",annual_roi())
print("total roi :",total_roi())

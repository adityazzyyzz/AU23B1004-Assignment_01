#3
def get_order(order):
    stack=[]

    l=0
    while l<=len(order)-1:
        print("preparing your order -",order[l])
        stack.append(order[l])
        l+=1

    stack=stack[::-1]
    print("the following orders have been dispatched")
    for _ in order:
        print(stack.pop())

c=["fried rice","noodles", "sandwich"]
get_order(c)
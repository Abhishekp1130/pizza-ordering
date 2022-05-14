


print("Welcome to python pizza deliveries")
size=input("what size of pizza do you want?s, m, l ")
addpeperoni=input("do you want pepperoni?y or n ")
extracheese=input("do you want extra cheese?y or n ")
print("small size pizza:15")
print("medium size pizza:20")
print("large size pizza:25")

print("pepperoni for small pizza:+2")
print("pepperoni for medium and large pizza:+3")

print("extra cheese:+1")
bill=0
if(size=="s"):
    bill+=15
elif(size=="m"):
    bill+=20
else:
    bill+=25
if addpeperoni=="y":
    if size=="s":
        bill+=2
else:
        bill+=3
if extracheese=="y":
    bill+=1
    print(f"your final bill is {bill}")
   
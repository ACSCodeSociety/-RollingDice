from random import randint
i = True
ans = input("Do you want to roll?")
while i : 
    if(ans  == "Yes"):
        print(randint(1,6))
        ans = input("Do you want to roll?")
    elif(ans == "No"):
           i=False
    

from random import randint
ans = input ('Do you want to roll a dice?')
kon = True
while kon == True:
  if ans == "yes":
    print(randint(1,6))
    ans = input ('Do you want to roll a dice?')
  elif ans == "no":
    kon = False

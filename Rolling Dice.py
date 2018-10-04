from random import randint
while True:
  roll = input("Do you want to roll a dice?")
  if roll == "yes":
   print(randint(1,6))
   continue
  elif roll == "no":
   print("Bye then!")
   break
  else:
   print("How rude!")
   break

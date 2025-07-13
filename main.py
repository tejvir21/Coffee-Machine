from time import *
import os
from str import *

available_resources={
  'Water': 500,
  'Milk': 1000,
  'Coffee': 150,
  'Sugar': 50,
  'Money': 0
}

os.system('clear')

while True:

  print()
  coffee_choice=input("What would you like to have?['Latte'/'Espresso'/'Cappuccino']\n")
  
  print()
  print()
  
  Rs_5_coin=0
  Rs_10_coin=0
  Rs_20_coin=0
  change=0
  temp_sum=0
  
  if coffee_choice.lower() == 'latte':
    
    if available_resources['Water'] >= 30 and available_resources['Milk'] >= 240 and available_resources['Coffee'] >= 30:
  
      print("Please insert coins")
      Rs_5_coin=int(input("How many Rs 5 coins: "))
      Rs_10_coin=int(input("How many Rs 10 coins: "))
      Rs_20_coin=int(input("How many Rs 20 coins: "))
      
      temp_sum = Rs_5_coin*5 + Rs_10_coin*10 + Rs_20_coin*20 
  
      if temp_sum >= 250:
        if temp_sum > 250:
          change = temp_sum - 250
        
        while True:
          want_sugar=input("Do you want to add sugar?['Yes' or 'No']\n")
          
          if want_sugar.lower() == 'yes' or want_sugar.lower() == 'y':
              how_much_sugar=int(input("How much spoon sugar you want to add?['1'/'2'/'3'/'4'/'5']\n"))
              
              if how_much_sugar*5 <= available_resources['Sugar']:
                available_resources['Sugar']-=(how_much_sugar*5)
                break
              else:
                print("This much sugar is not available..")
                continue
          elif want_sugar.lower() == 'no' or want_sugar.lower() == 'n':
            break
      else:
        print("Not Enough Money..")
        continue
  
      available_resources['Water']-=30
      available_resources['Milk']-=240
      available_resources['Coffee']-=30 
      available_resources['Money']+=250
  
      print()
      print(f"Here is your Rs {change} change.")
      print()
      print(f"Here is your {coffee_choice}.")
      print()
      continue
       
    else:
      if available_resources['Water'] < 30:
        print("Sorry there is not enough water")
      if available_resources['Milk'] < 240:
        print("Sorry there is not enough milk")
      if available_resources['Coffee'] < 30:
        print("Sorry there is not enough coffee")
      continue
  
  elif coffee_choice.lower() == 'cappuccino':
    
    if available_resources['Milk'] >= 120 and available_resources['Coffee'] >= 30:
  
      print("Please insert coins")
      Rs_5_coin=int(input("How many Rs 5 coins: "))
      Rs_10_coin=int(input("How many Rs 10 coins: "))
      Rs_20_coin=int(input("How many Rs 20 coins: "))
      
      temp_sum = Rs_5_coin*5 + Rs_10_coin*10 + Rs_20_coin*20 
  
      if temp_sum >= 300:
        if temp_sum > 300:
          change = temp_sum - 300
        while True:
          want_sugar=input("Do you want to add sugar?['Yes' or 'No']\n")
          
          if want_sugar.lower() == 'yes' or want_sugar.lower() == 'y':
              how_much_sugar=int(input("How much spoon sugar you want to add?['1'/'2'/'3'/'4'/'5']\n"))
              
              if how_much_sugar*5 <= available_resources['Sugar']:
                available_resources['Sugar']-=(how_much_sugar*5)
                break
              else:
                print("This much sugar is not available..")
                continue
          elif want_sugar.lower() == 'no' or want_sugar.lower() == 'n':
            break
      else:
        print("Not Enough Money..")
        continue
        
      available_resources['Milk']-=120
      available_resources['Coffee']-=30 
      available_resources['Money']+=300
  
      print()
      print(f"Here is your Rs {change} change.")
      print()
      print(f"Here is your {coffee_choice}.")
      print()
      continue
       
    else:
      if available_resources['Milk'] < 120:
        print("Sorry there is not enough milk")
      if available_resources['Coffee'] < 30:
        print("Sorry there is not enough coffee")
      continue
  
  elif coffee_choice.lower() == 'espresso':
    
    if available_resources['Water'] >= 120 and available_resources['Milk'] >= 120 and available_resources['Coffee'] >= 10:
  
      print("Please insert coins")
      Rs_5_coin=int(input("How many Rs 5 coins: "))
      Rs_10_coin=int(input("How many Rs 10 coins: "))
      Rs_20_coin=int(input("How many Rs 20 coins: "))
      
      temp_sum = Rs_5_coin*5 + Rs_10_coin*10 + Rs_20_coin*20 
  
      if temp_sum >= 200:
        if temp_sum > 200:
          change = temp_sum - 200
        while True:
          want_sugar=input("Do you want to add sugar?['Yes' or 'No']\n")
          
          if want_sugar.lower() == 'yes' or want_sugar.lower() == 'y':
              how_much_sugar=int(input("How much spoon sugar you want to add?['1'/'2'/'3'/'4'/'5']\n"))
              
              if how_much_sugar*5 <= available_resources['Sugar']:
                available_resources['Sugar']-=(how_much_sugar*5)
                break
              else:
                print("This much sugar is not available..")
                continue
          elif want_sugar.lower() == 'no' or want_sugar.lower() == 'n':
            break
            
      else:
        print("Not Enough Money..")
        continue
  
      available_resources['Water']-=120
      available_resources['Milk']-=120
      available_resources['Coffee']-=10 
      available_resources['Money']+=200
  
      print()
      print(f"Here is your Rs {change} change.")
      print()
      print(f"Here is your {coffee_choice}.")
      print()
      continue
       
    else:
      if available_resources['Water'] < 120:
        print("Sorry there is not enough water")
      if available_resources['Milk'] < 120:
        print("Sorry there is not enough milk")
      if available_resources['Coffee'] < 10:
        print("Sorry there is not enough coffee")
      continue
  
  elif coffee_choice.lower() == 'report':
    print("Here is coffee machine report:-")
  
    for i in available_resources:
      if i == 'Sugar':
        print(i,":",available_resources[i],"g")
      elif i == 'Money':
        print(i,":","Rs",available_resources[i])
      else:
        print(i,":",available_resources[i],"ml")
    continue
  
  elif coffee_choice.lower() == 'off':
    print("Refilling Resources",end="")
    sleep(1)
  
    for i in range(5):
      print(".",end="")
      
    print()
    print("Turning off..")
    sleep(2)
    break
  
  elif coffee_choice.lower() == 'menu':
    print("       Cafe Menu:-")
    print()
    print("Cappuccino            300/-")
    print("Latte                 250/-")
    print("Espresso              200/-")
    continue

os.system("clear")
print("Coffee machine")
print("        -By Tejvir Chauhan")

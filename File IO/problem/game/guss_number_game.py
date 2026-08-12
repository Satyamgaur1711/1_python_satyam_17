import datetime
import random

g_level = int(input("enter the level of game you want to play within (1,10)"))


bot_num = random.randint(1, 10**g_level)

print(f"guess the number between 1 {10**g_level}")

guss_history = []
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

x = 0
count = 0+10*g_level
while x != bot_num:
 usr_ipt = int(input())
 guss_history.append(f"your inputs are {current_time} {usr_ipt}")

 x = usr_ipt
 count -=1
 if usr_ipt>bot_num :
  print("too large thoda chota dali")
 elif usr_ipt<bot_num :
  print("small -- bada dalo")
 else:
  print("you guess correctly")

print(count)





with open("high_score.txt", "w") as f:
 
 f.write(str(count))




with open("Deta_guss.txt" "w") as k:
 k.write(f"{g_level} is the game level \n")
 for record in guss_history:
  k.write(record + "\n")

print("your score is ", str(count))


    

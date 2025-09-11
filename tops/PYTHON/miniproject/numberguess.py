import random

target_number = random.randint(1, 100)
guess = True

print("gusse number between 1 to 100 ")
while guess:
        num = int(input("Enter your guess: "))
        
        if num < target_number:
            print("Too low")
        elif num > target_number:
            print("Too high")
        else:
            print("you win")
            guess = False

# ========================================= level 2 ========================================================

level2 = input("you want to play level 2?(yes/no): ").lower()

if level2 == 'yes':
     print("gusse number between 1 to 200 ")
     target_number = random.randint(1,200)
     guess = True

     while guess:
          num = int(input("enter your guess: "))
          if num < target_number:
               print("too low")
          elif num > target_number:
               print("too high")
          else:
               print("you win")
               guess = False

#  =================================================== level 3 ==============================================

level3 = input("you want to play level 3?(yes/no): ").lower()

if level3 == 'yes':
     print("guess the number between 1 to 200 but only in 10 attemps.")
     target_number = random.randint(1,200)
     guess = True
     atmpt = 0
     max_atmpt = 10

     while guess and atmpt < max_atmpt:
          num = int(input(f"{atmpt+1}/{max_atmpt} enter your guess: "))
          atmpt+=1

          if num == target_number:
               print(f"you win!! you guess in {atmpt}")
               guess = False
          else:
               if num < target_number:
                    print("too low")
               else:
                    print("too high")
     if guess:
          print(f"game over you use all {max_atmpt} and the number is {target_number}")
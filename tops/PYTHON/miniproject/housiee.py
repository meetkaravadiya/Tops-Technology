import random 

print("------------------------welcome to housiee ----------------------")

ticket = random.sample(range(1,101),12)

random.shuffle(ticket)

p1 = ticket[:6]
p2 = ticket[6:]

print("player 1 :", p1)
print("player 2 : ", p2)

while p1 != [] and p2 != []:
        input("------------ press enter to draw number ---------------")
    
        num = random.choice(ticket)
        print(f"the number is {num}")

        if num in p1:
            p1.remove(num)
            print(f"player 1 have the number {num}.")
            print("-------------------------------------------------")

        if num in p2:
            p2.remove(num)
            print(f"player 2 have the number {num}.")
            print("-------------------------------------------------")
    
        ticket.remove(num)
    
        print(f"player 1 : {p1}")
        print(f"player 2 : {p2}")

if p1 == []:
     print("player 1 win the game!!!!!")
if p2 == []:
     print("player 2 win the game!!!!")

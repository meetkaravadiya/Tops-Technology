import random 

print("------------------------welcome to housiee ----------------------")

player1 = input("enter player1 name: ")
player2 = input("enter player2 name: ")

ticket = random.sample(range(1,101),12)

random.shuffle(ticket)

p1 = ticket[:6]
p2 = ticket[6:]

print(f"{player1} :", p1)
print(f"{player2} : ", p2)

while p1 != [] and p2 != []:
        input("------------ press enter to draw number ---------------")
    
        num = random.choice(ticket)
        print(f"the number is {num}")

        if num in p1:
            p1.remove(num)
            print(f"{player1} have the number {num}.")
            print("-------------------------------------------------")

        if num in p2:
            p2.remove(num)
            print(f"{player2} have the number {num}.")
            print("-------------------------------------------------")
    
        ticket.remove(num)
    
        print(f"{player1} : {p1}")
        print(f"{player2} : {p2}")

if p1 == []:
     print("-----------------------------")
     print(f"{player1} win the game!!!!!")
if p2 == []:
     print("------------------------------")
     print(f"{player2} win the game!!!!")

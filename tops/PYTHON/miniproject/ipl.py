import random

print("-----------------------super over match-------------------------")

# ============================= team ====================================================

team = ['CSK','RR','KKR','MI','RCB','GT','LSG','SRH','DC','KXIP']

print("choose your team: ", team)

mt = input("enter your team: ").upper()

if mt not in team:
    print("choose from upper team ")
else:
    print("your team: ",mt)
    team.remove(mt)
    opp = random.choice(team)
    print("opp team: ",opp)
# ====================================== toss bat ball ==============================================
toss = ['H','T']
dic = ['BAT','BALL']

choose = input("choose Toss h/t: ").upper()

if choose == random.choice(toss):
    print(f"{mt} won the toss")
    pick = input("choose bat/ball: ").upper()
    if pick == "BAT": 
        batfirst = mt
        bowlfirst = opp
        print(f"{mt} choose to bat first")
    else:
        batfirst = opp
        bowlfirst = mt
        print(f"{mt} choose to ball first")
else:
    print(f"{opp} won the toss")
    pick = random.choice(dic)
    if pick == "bat": 
        batfirst = opp
        bowlfirst = mt
        print(f"{opp} choose to bat first")
    else:
        batfirst = mt
        bowlfirst = opp
        print(f"{opp} choose to ball first")

# ==================================== 1st innings ========================================================

result = [0,1,2,3,4,6,"w","no ball"]
balls = 6
run = 0
wicket = 0
ball = 0
print(f"{batfirst}: {run}/{wicket} ({ball})")
overball = f"0.{ball}"

while ball < 6 and wicket < 1:
    input("------------------ press enter for ball ----------------------")
    
    c1 = random.choice(result)
    if c1 == 'no ball':
        pass
    elif ball < 5:
       overball = f"0.{ball+1}"
    else:
        overball = "1"


    if c1 in [0,1,2,3,4,6]:
        run += c1
        ball += 1
        print(f"{c1} runs")
        print(f"{batfirst}: {run}/{wicket} ({overball})")
    
    if c1 == 'no ball':
        run +=1
        print(f"{c1}!!")
        print(f"{batfirst}: {run}/{wicket} ({overball})")
        

    if c1 == 'w':
        wicket+=1
        print(f"it is wicket")
        print(f"{batfirst}: {run}/{wicket} ({overball})")
    

print(f"{bowlfirst} need {run+1} runs in {balls} balls to win")
print()

# ======================================= 2nd innigs ==================================================

input("press enter to start 2nd innings")

balls = 6
run1 = 0
wicket = 0
ball = 0
overball = f"0.{ball}"


print(f"{bowlfirst}: {run1}/{wicket} ({ball})")


while ball < 6 and wicket< 1 and run+1 > run1:
    input("------------------ press enter for ball ----------------------")
    
    c1 = random.choice(result)
    if c1 == 'no ball':
        pass
    elif ball < 5:
        overball = f"0.{ball+1}"
    else:
        overball = "1"

    if c1 in [0,1,2,3,4,5,6]:
        run1 += c1
        ball += 1
        balls -= 1
        print(f"{c1} runs")
        print(f"{bowlfirst}: {run1}/{wicket} ({overball})")

    
    if c1 == 'no ball':
        run1 +=1
        print(f"{c1}!!")
        print(f"{bowlfirst}: {run1}/{wicket} ({overball})")


    if c1 == 'w':
        wicket+=1
        print(f"it is wicket")
        print(f"{bowlfirst}: {run1}/{wicket} ({overball})")

    if wicket < 1 and run+1 > run1 and ball < 6 :
        print(f"{bowlfirst} need {(run+1)-run1} runs in {balls} balls to win")


# ==================================================  result ================================================

if run > run1:
    print("-----------------------------------")
    print(f"{batfirst} win the match")
    print("------------------------------------")
else:
    print("-------------------------------------")
    print(f"{bowlfirst} win the match")
    print("--------------------------------------")

if run == run1:
    print("-----------------------------------------")
    print(f"{mt} vs {opp} match is draw")
    print("-----------------------------------------")
import random

'''
  1 for rock
  0 for paper
  -1 for scissor
'''

computer = random.choice([1,0,-1])

commandingMsg=print("Please enter s->Scissor, p->Paper, r->Rock ")
playerInput= input("Enter your choice: ")

playerDict={
    "r":1,
    "p":0,
    "s":-1
}
computerDict={
    1:"Rock",
    0:"Paper",
    -1:"Scissor"
}

player=playerDict[playerInput]

print(f"You choose {computerDict[player]}")
print(f"Computer choose {computerDict[computer]}")

if(computer==player):
    print("Draw")

else:
    if(computer==1 and player ==-1):
        print("You lost")

    elif(computer==1 and player==0):
        print("You win")

    elif(computer==0 and player==1):
        print("You lost")

    elif(computer==0 and player==-1):
        print("You win")

    elif(computer==-1 and player==0):
        print("You lost")

    elif(computer==-1 and player==1):
        print("You won")

    else:
        print("Something went wrong, please check your choice..")


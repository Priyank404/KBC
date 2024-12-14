import time
from questons import game
print("\n\n\t\t\t\t\t\t!!!KON BANEGA CROREPATI!!!\n")
print("\t\t\t\t\t\t    WELCOM TO THE GAME \n\n \t\t\t\tHERE YOU CAN WIN INCRADABLE AMOUNT OF PRIZE JUST BY GIVING ANSWER")


winPrize=1000
for i,question in enumerate(game,1):
    print("QUESTION WILL APPEAR IN 3s\n")
    time.sleep(3)
    print(f"Q{i}: {question['question']} for {winPrize}rs")
    for option in question['options']:
        print(f"{option}")
    ans=input("enter your answer: ")
    print("\n\t\t\t\t\t\t\tARE YOU SURE ????\n\t\t\t\t\t\tHEART BEATS ARE INCREASING........")
    time.sleep(5)
    if(ans==question['answer']):
        print(f"\n\t\t\t\t\t\t!!!CONGRATULATION YOU WON {winPrize}!!!\n")
        if(i==1):
            winPrize=5000
        elif(i>=2 and i<=5):
            winPrize=winPrize+5000
        else:
            winPrize=winPrize+10000
    else:
        print(f"\n\n\t\t\t\t\t\t\tWRONG ANSWER\nYOU LOOSE {winPrize} \n BETTER LUCK NEXT TIME ")
        break   






        


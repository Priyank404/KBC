import time
from questons import game  # bring the question file

terminal_width=130   # this can be change based on your terminal size
print("\n"+"!!!KON BANEGA CROREPATI!!!\n\n".center(terminal_width))      # .center is use to place the text in center 
print("WELCOM TO THE GAME\n\n".center(terminal_width))
print("HERE YOU CAN WIN INCRADABLE AMOUNT OF PRIZE JUST BY GIVING ANSWER".center(terminal_width))


winPrize=1000
for i,question in enumerate(game,1):  # this loop will iterate through list of questions
    print("QUESTION WILL APPEAR IN 3s\n")
    time.sleep(3)
    print(f"Q{i}: {question['question']} for {winPrize}rs")
    for option in question['options']:
        print(f"{option}")
    ans=input("enter your answer: ")
    print("ARE YOU SURE ????".center(terminal_width))
    print("HEART BEATS ARE INCREASING........".center(terminal_width))
    time.sleep(5)
    if(ans==question['answer']):
        print("\n"+f"!!!CONGRATULATION YOU WON {winPrize}!!!".center(terminal_width))

        # this will increase the prize based on the number of question

        if(i==1):
            winPrize=5000
        elif(i>=2 and i<=5):
            winPrize=winPrize+5000
        else:
            winPrize=winPrize+10000
    else:
        print("\n"+f"WRONG ANSWER".center(terminal_width))
        print(f"YOU LOOSE {winPrize}")
        print("BETTER LUCK NEXT TIME".center(terminal_width))
        break

print("\n"+f"YOU TAKE Rs{winPrize} AT HOME!!!".center(terminal_width))
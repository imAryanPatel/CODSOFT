import random

user = input("Select the option (STONE :st / PAPER:p / SCISSORS:sc): ")
choice = ['st' , 'p' , 'sc']
comp = random.choice(choice)
print(f"Computer choice: {comp}")

if user == comp:
    print("Tie")
elif (user == 'st' and comp == 'sc') or \
     (user == 'p' and comp=='st') or \
     (user == 'sc' and comp=='p') :
    print('U win')
elif user in choice:
    print('U lose')
else:
    print("invalid")

import random
print('guess the number game')
c=random.randint(1, 30)

def numberguess():
    x=int(input('Hey please enter the number between [1:30]:'))
    if x==c:
        print('yes the correct number is',x)
    elif x!=c:
        print('please try again bro')
        #print(f'the correct number was {c} please try again')
        numberguess()
    
numberguess()

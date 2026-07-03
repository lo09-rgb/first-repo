print('Parity checker')
def paritycheck(n):
    new_list=[]
    n=int(input('Enter the number you want to check the parity for:'))
    if n%2==0:
        print('even number as input ')
    print('the number is odd')
    c=str(n)
    for i in c:
        new_list.append(int(i))
        x=sum(new_list[0:len(new_list)+1])
    if x%2==0:
        print('The sum is even')
    print('the sum is odd ')
    if n%2==x%2:
        print('yes its a parity')
    print('not a parity')
paritycheck(n)

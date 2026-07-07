n=int(input('enter the number of people  in the circle:'))
def josephus():
    if n < 1:
        return False

    winner = 0

    for i in range(2, n + 1):
        winner = (winner + 2) % i

    return 'winner is the person',winner
josephus()

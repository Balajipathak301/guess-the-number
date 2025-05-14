"""hidden numbers
can only take 9 guesses
if wrong game over
if correct game over
number of guesses
number between 1-100"""
print("enter a number between 1-100")
n=1
while (n<10):
    i=int(input())
    if i==18:
        print("number was 18 , You won")
        print("number of guesses-", n)
        print("game over")
    elif i>18:
        print("try a smaller number")
    else:
        print("try a greater number")
    n=n+1
if n>9:
    print("chances over , You lost")
    print("number of guesses-", n-1)
    print("Game over")
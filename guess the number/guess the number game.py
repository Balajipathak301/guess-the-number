"""hidden numbers
can only take 9 gusses
if wrong game over
if correct game over
number between 1-100"""
print("enter a number between 1-100")
n=0
while (n<9):
    i=int(input())
    if i==18:
        print("number was 18 , You won")
        print("game over")
    elif i>18:
        print("try a smaller number")
    else:
        print("try a greater number")
    n=n+1
if n>8:
    print("chances over , You lost")
    print("game over")
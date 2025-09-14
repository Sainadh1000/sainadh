import random
while True:
    num=random.randint(1,100)
    count=0
    while True:
        guess=int(input("my guess:"))
        count+=1
        if guess>num:
            print("Too high")
        elif guess<num:
            print("too low")
        else:
            print(f"correct! you guessed number in {count} tries")
            break
    playagain=input("want to play again(yes/no):")
    if playagain.lower()!="yes":
        break

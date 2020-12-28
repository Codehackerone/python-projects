from numpy import random

print("Guess the number Challenge!!\nThe Number Lies Between 1 and 100\n")
hint = []
div = [47, 43, 41, 39, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]
great = []
low = []
points = 50
number = random.randint(100)
number += 1
congrats = 0
ch = [0, 1, 2, 3]
i = 1
while i < 6:
    for x in hint:
        print(x)
    n = input("Guess the number :")
    n = int(n)
    if n < 1 or n > 100:
        print("Enter between 1 and 100")
        continue
    elif n == number:
        print("Congrats!! You have guessed the number correctly!!\nPoints", points)
        congrats = 1
        break
    else:
        points = points - 10
        choice = random.choice(ch)
        if choice == 0:
            while True:
                greater = random.randint(100) + 1
                if greater in great:
                    continue
                elif greater > number:
                    break
                else:
                    continue
            j = str(i)
            great.append(greater)
            k = str(greater)
            hint.append("Hint " + j + ": The number is lower than " + k)
        elif choice == 1:
            while True:
                lower = random.randint(100) + 1
                if lower in low:
                    continue
                elif lower < number:
                    break
                else:
                    continue
            j = str(i)
            great.append(lower)
            k = str(lower)
            hint.append("Hint " + j + ": The number is greater than " + k)
        elif choice == 2:
            j = str(i)
            if number % 2 == 0:
                hint.append("Hint " + j + ": The number is even")
            else:
                hint.append("Hint " + j + ": The number is odd")
            ch.remove(2)
        elif choice == 3:
            j = str(i)
            m = 0
            for x in div:
                if number % x == 0:
                    k = str(x)
                    hint.append("Hint " + j + ": The number is divisible by " + k)
                    m = 1
                    break
            if m == 0:
                hint.append("Hint " + j + ": The number is prime ")
            ch.remove(3)
    i = i + 1
if congrats == 0:
    print("Looks like You Lost!! The number was ", number)

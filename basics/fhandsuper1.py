import os

while True:
    filename = input("Enter a new text file name:")
    filename = filename + ".txt"
    if os.path.exists(filename):
        print("The file already exists. Choose another file name!")
    else:
        f = open(filename, "x")
        f.close()
        break
while True:
    n = input("What do you want to do:\n1.Add text\n2.Read text\n3.Rewrite text\n4.Delete text\n5.Delete File\n6.Exit\n")
    n=int(n)
    if not type(n) is int:
        print("Please Choose a number")
        print(type(n))
        continue
    if n > 6 or n < 1:
        print("Choose a number between 1 and 6")
        continue
    elif n == 6:
        print("Exit")
        break
    else:
        if n == 1:
            text = input("Enter text to add to file:")
            f = open(filename, "a")
            f.write(text)
            f.close()
            print("Text Added Successfully!")
        elif n == 2:
            f = open(filename, "r")
            print(f.read())
            f.close()
        elif n == 3:
            text = input("Enter text to rewrite to file:")
            f = open(filename, "w")
            f.write(text)
            f.close()
            print("Text Rewritten Successfully!")
        elif n == 4:
            f = open(filename, "w")
            f.close()
            print("Text Deleted Successfully!")
        elif n == 5:
            os.remove(filename)
            print("File Removed Successfully!")
            break

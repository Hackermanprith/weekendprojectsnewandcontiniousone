number = int(input("Enter your number: "))
temp=number
rev = 0
while (number>0):
    lol=number%10
    rev = rev*10+lol
    number = number//10

if temp == rev:
    print("Num is palindrom")
else:
    print("Not palindrom")
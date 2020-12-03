y = x = int(input("Enter a number."))
palin = 0
while y > 0:
    palin = (palin * 10) + (y % 10)
    y //= 10
print(palin)
if palin == x:
    print("A palindrome number.")

else:
    print("Not a palindrome number.")
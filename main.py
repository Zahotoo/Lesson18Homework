# Homework
# Write a program that asks for a 4-digits number that is even and also does not end with a 0.
# 1235 IS BAD BECAUSE IT IS NOT EVEN
# 1236 IS GOOD BECAUSE IT IS EVEN
# 1230 IS BAD BECAUSE IT ENDS WITH 0
# 123 IS BAD BECAUSE IT IS NOT 4-DIGITS
# 12345 IS BAD BECAUSE IT IS NOT 4-DIGITS
x = int(input("Please give me a 4-digits number: "))

if 0 < x < 1000 or x > 9999:
    print(x,"is bad because it is not 4-digits number.")
elif x >= 1000 and x <= 9999:
    if x % 2 == 0:  # If the remainder is 0, can show that the number is a even.
        if x % 10 != 0:  # If the remainder is not 0, can show that the number does not end with 0.
            print(x, "is good because it is even.")
        else:
            print(x, "is bad because it ends with 0.")
    else:
        print(x, "is bad because it is not even.")
else:
    print(x, "is bad because it is a negative number.")

quit()







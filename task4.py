#1.ASCII value of a character

# a=input("Enter a character:")
# print("The ASCII value of" + a + "is",ord(a))

#2.ASCII value of all character

# import string
#
# for c in string.ascii_uppercase:
#     print(f'ASCII for {c} is {ord(c)}')
# for c in string.ascii_lowercase:
#     print(f'ASCII for {c} is {ord(c)}')

#3.Largest of 3 numbers

# a=int(input("Enter first no:"))
# b=int(input("Enter second no:"))
# c=int(input("Enter third no:"))
# if a>b:
#     print("Largest no is",a)
# elif b>c:
#     print("Largest no is",b)
# else:
#     print("Largest no is",c)

#4.Reverse of a number

# a=int(input("Enter a no:"))
# rev=0
# while (a > 0):
#     dig = a % 10
#     rev = rev * 10 + dig
#     a = a // 10
# print("The reverse of the number:", rev)

#5.Leap year or not

# a=int(input("Enter a year:"))
# if (a%400==0)or (a%4==0 and a%100!=0):
#     print("Leap year")
# else:
#     print("Not a leap year")
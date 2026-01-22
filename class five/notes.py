# attendancePerc = int(input("enter your attendance percentage: "))
# if attendancePerc > 75:
#     print("your eligible for the exam")
# else:
#     print("your not eligible for the exam")


# num = int(input("enter a number:"))
# rem = num % 2
# print(f"num {num}, reminader : {rem}")

# if rem == 0:
#     print("num is even")
# else:
#     print("num is odd")

# num = int(input("give me a num:"))
# rem = num % 3
# if rem == 0:
#     print("is divisible")
# else:
#     print("not dividsible")

num = int(input("give me a num: "))
rem = num % 3 and num % 5
if rem == 0:
    print("is divisible")
else:
    print("not divisible")
# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/20 15:39
# 文件名称：input.py
# 开发软件：PyCharm
message=input("What car do you want to rent?")
print("Let me see if I can find you a {}.".format(message))

inquiry=int(input("How many people need to eat?"))
if inquiry > 8:
    print("There is no empty table.")
else:
    print("Free table!")

number=int(input("Enter a number,and I will tell you if it's multiple of 10:"))
if number % 10 == 0:
    print("\nThe number {} is a multiple of 10.".format(number))
else:
    print("\nThe number {} is not a multiple of 10.".format(number))

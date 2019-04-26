# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/20 15:29
# 文件名称：even_or_odd.py
# 开发软件：PyCharm
number=int(input("Enter a number,and I'll tell you if it's even or odd:"))
if number % 2 == 0:
    print("\nThe number {} is even.".format(number))
else:
    print("\nThe number {} is odd.".format(number))
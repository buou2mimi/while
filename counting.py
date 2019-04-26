# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/20 15:53
# 文件名称：counting.py
# 开发软件：PyCharm
current_number=1
while current_number <= 5:
    print(current_number)
    current_number += 1

current_number2=0
while current_number2 < 10:
    current_number2+=1
    if current_number2 % 2 == 0:
        continue
    print(current_number2)
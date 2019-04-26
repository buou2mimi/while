# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/20 17:39
# 文件名称：while4.py
# 开发软件：PyCharm
prompt="Please enter your age,I will tell you ticket price."
prompt+="\n(Enter 'quit' when you finished.)"
age=""
active=True
while active:
    age=input(prompt)
    if age=="quit":
        active=False
    else:
        age=int(age)
        if age < 3:
            print("Free viewing!")
        elif 3 <= age <= 12:
            print("You need to pay $10 for ticket.")
        elif age > 12:
            print("You need to pay $15 for ticket.")

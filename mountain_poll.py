# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/20 20:42
# 文件名称：mountain_poll.py
# 开发软件：PyCharm
responses={}        #定义空字典
polling_active = True       #定义一个标志
while polling_active:
    name=input("\nWhat is your name?")      #输入名字作为键
    response=input("Which mountain would you like to climb someday?")       #输入山名作为值
    responses[name]=response        #将输入的键值对应输入定义的字典中
    repeat=input("Would you like to let another person respond?(yes/no)")       #询问是否询问其他人信息
    if repeat == "no":
        polling_active=False
print("\n---Poll Results---")       #显示调查结果
for name,response in responses.items():
    print("{} would like to climb {}.".format(name,response))
# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/20 17:34
# 文件名称：while3.py
# 开发软件：PyCharm
prompt="Please enter the pizza ingredient you want:"
prompt+="\n(Enter 'quit' when you finished.)"
ingredient=""
active=True
while active:
    ingredient=input(prompt)
    if ingredient != "quit":
        print("We will add {} to your pizza.".format(ingredient))
    else:
        active=False
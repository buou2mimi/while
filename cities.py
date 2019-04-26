# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/20 16:42
# 文件名称：cities.py
# 开发软件：PyCharm
prompt="\nPlease enter the name of a city you have visited:"
prompt+="\n(Enter 'quit' when you are finished.)"
while True:
    city=input(prompt)
    if city == "quit":
        break
    else:
        print("I'd love to go to {}!".format(city.title()))
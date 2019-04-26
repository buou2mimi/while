# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/21 14:19
# 文件名称：while10.py
# 开发软件：PyCharm
dream_resorts={}
polling_activer=True
while polling_activer:
    name=input("What is your name?")
    dream_resort=input("If you could visit one place in the world,where would you go?")
    dream_resorts[name]=dream_resort
    repeat=input("Do you want to konw others' thoughts?(yes/no)")
    if repeat=="no":
        polling_activer=False
print("\n---Poll Results---")
for name,dream_resort in dream_resorts.items():
    print("{} would like to go to {} for vacation.".format(name.title(),dream_resort.title()))
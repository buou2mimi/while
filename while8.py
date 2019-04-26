# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/20 21:19
# 文件名称：while8.py
# 开发软件：PyCharm
sandwich_orders=['tuna sandwich','mushroom sandwich','cheese sandwich']
finished_sandwiches=[]
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print("I made your {}.".format(sandwich))
    finished_sandwiches.append(sandwich)
print("\nI made the following sandwiches:")
for sandwiches in finished_sandwiches:
    print("\t{}".format(sandwiches))
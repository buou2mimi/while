# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/20 20:37
# 文件名称：pets.py
# 开发软件：PyCharm
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
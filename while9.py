# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/20 21:40
# 文件名称：while9.py
# 开发软件：PyCharm
sandwich_orders=['pastrami sandwich','tuna sandwich','pastrami sandwich','mushroom sandwich','cheese sandwich','pastrami sandwich']
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
print(sandwich_orders)
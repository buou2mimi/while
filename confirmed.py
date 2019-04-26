# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/20 20:11
# 文件名称：confirmed.py
# 开发软件：PyCharm
unconfirmed_users=['alice','brian','candace']  #创建一个待验证用户列表
confirmed_users=[]                             #一个用于储存已验证用户的空列表
while unconfirmed_users:                       #验证每个用户，知道没有未验证用户为止
    current_user=unconfirmed_users.pop()       #将每个未验证用户从列表中移除，赋予中间变量，在依次加入已验证用户列表
    print("Verifying user:{}".format(current_user.title()))
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
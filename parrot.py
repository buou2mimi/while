# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/20 15:59
# 文件名称：parrot.py
# 开发软件：PyCharm
"""prompt="\nTell me something,and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."
message=""
while message != "quit":
    message=input(prompt)
    if message != "quit":
        print(message)"""

prompt="\nTell me something,and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."
active=True
while active:
    message = input(prompt)
    if message == "quit":
        active=False
    else:
        print(message)

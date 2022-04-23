list = ['yong3', 'wang3', 'zhi2']
str = ""
for i in list:
    str = str + i
newstring = ''.join([i for i in str if not i.isdigit()])
#print(newstring)
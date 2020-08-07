names = ["Songsa","Liupengjuan",["Maroom,lee"],"Songss"]
#print(names[0])
names.append("SongNI")
names.insert(2,"Liuyi")
names[2]="songliuyi"
names.remove("Songss")
del names[2]
names.pop()
idx = names.index("Liupengjuan")
print(names.count("SongSa"))
names.clear()
names.reverse()
names.sort()
names2=["i love you","baby",["tom","jack"],"1314"]
names.extend(names2)
# print(names[0:3])#切片
# print(names[:3])#切片
# print(names[1:3])#切片
# print(names[-1])
# print(names[-3:-1])
# print(names[-3:])
names_1=names.copy()#浅copy
names2[2][1]="宋洒"
names2[0]="我爱你"
print(names2)
import copy
names = copy.deepcopy(names2)
print(names)
print(names[0:-1:2])
print(names[::2])
print(names[:])#全部打印 没有人这样写

#浅拷贝的三种方式
person=['name',['songsa',99]]

p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)
#浅拷贝用来创建联合账号

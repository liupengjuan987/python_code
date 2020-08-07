provice=open("D:\homework\provinces.txt","r", encoding="utf-8")
lines=provice.readlines()
print(type(lines))
for index in range(len(lines)):
    print(lines[index])
num=int(input("请输入要选择的省份前数字："))
city=open("D:\homework\citys.txt","r", encoding="utf-8")
line=city.readlines()
for idx in range(len(line)):
    info=line[idx].strip().split(",")
    pro_id=int(info[3].strip())
    if pro_id == num:
        print(info)
choose=int(input("请选择市前数字或Q退出："))
if choose == "Q":
    exit(0)
areas = open(r"D:\homework\bbreas.txt", "r", encoding="utf-8")
lines = areas.readlines()
for idx in range(len(lines)):
    info = lines[idx].strip().split(",")
    area_id=int(info[3].strip())
    if area_id == choose :
        print(info)
choose = int(input("请选择具体地址前数字或Q退出："))
print(lines[choose-1])


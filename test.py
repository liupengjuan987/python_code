provice=open("D:\homework\provinces.txt","r", encoding="utf-8")
lines=provice.readlines()
print(type(lines))
for index in range(len(lines)):
    print(lines[index])
num=int(input("请输入要选择的省份前数字："))
city=open("D:\homework\citys.txt","r", encoding="utf-8")
line=city.readlines()
#print(line)
#print("************")
for idx in range(len(line)):
    #print(idx,line[idx])
    infos=line[idx].strip().split(",")

    if int(infos[3].strip()) == num:
        print("Good!")
        print(infos)
        #print("good!")
    #print(type(line[idx].split(",")))
    # if info[3] == num:
    #     print(info)
    #     choose=int(input("请选择数字或Q退出："))
    #     if choose == "Q":
    #         exit(0)
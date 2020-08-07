salary=int(input("你的工资："))
#list=((1,"Iphone",5000),(2,"bike",400))
list2=[[1,"Iphone",5000],[2,"bike",400],[3,"Tesla",230000],[4,"ningde",20000]]
list=[]
#print(len(list2))
while True:
    for i in range(len(list2)):
        print(list2[i])
    num = input("请选择要购买的商品编号：/Q 退出")
    if num != "Q":
        num = int(num)
        if list2[num-1][2] <= salary:
            print("已购买商品{num}".format(num  = list2[num-1]))
            salary = salary - list2[num-1][2]
            print("您的余额为：{salary}".format(salary=salary))
            list.append(list2[num-1])
        else:
            print("余额不足")
            print("已购买商品列表如下")
            print(list)
            # for i in range(len(list)):
            #     print(list[i])
            break
    elif num == "Q":
        exit(0)

    # for j in range(len(list2[i])):
    #     print(list2[i][j])

data = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家","安家"]
        },
        "朝阳":{
            "望京":["benz","momo"],
            "东直门":["飞信","HP"]
        },
        "海淀":{
            "西二旗":["oldboy","test"],
            "上地":["链家","安家"]
        },
    },
    '山东':{
        "济南":{
            "沙河":["oldboy","test"],
            "天通苑":["链家","安家"]
        },
        "菏泽":{
            "东明县":["oldboy","test"],
            "天通苑":["链家","安家"]
        }
    },
    '陕西':{
        "西安":{
            "雁塔区":["oldboy","test"],
            "长安区":["链家","安家"]
        },
        "咸阳":{
            "沙河":["oldboy","test"],
            "天通苑":["链家","安家"]
        }
    }
}
exit_flag = False
while not exit_flag:
    for i in data:
        print(i)
    choose = input("选择1>>>:")
    if choose in data:
        while not exit_flag:
            for j in data[choose]:
                print("\t",j)
            choice = input("请选择2>>>:")
            if choice in data[choose]:
                while not exit_flag:
                    for k in data[choose][choice]:
                        print("\t",k)
                    ch = input("选择3>>>:")
                    if ch in data[choose][choice]:
                        for z in data[choose][choice][ch]:
                            print(z)
                        chs = input("最后一层按b返回>>>:")
                        if chs == "b":
                            pass
                        elif chs == 'q':
                            exit_flag = True
                    if ch == "b":
                        break
                    elif ch == 'q':
                        exit_flag = True
            if choice == "b":
                break
            elif choice == 'q':
                exit_flag = True
    if choose == "b":
        break
    elif choose == 'q':
        exit_flag = True
# info = {
#     'stu01':"SongSa",
#     'stu02':"Liupengjuan",
#     'stu03':"SongLiuyi"
# }
# b = {
#     '菜':"宫保鸡丁",
#     1:3,
#     2:6
# }
# c2 = info.fromkeys([6,7,8])
# c = info.fromkeys([6,7,8],"test")
# c = info.fromkeys([6,7,8],[1,{"name":"Songss"},666])
# print(c)
# info.update(b)
# print(info)
# print(info.items())
# info.setdefault('stu01',"贼娃子")
# info.setdefault('stu04',"贼娃子")
# print(info)
# # info['stu03']="贼娃子"
# # info['stu05']="贼娃子"
# # #del info['stu05']
# # #info.pop('stu03')
# # #info.popitem()
# # #print(info.get('stu03'))
# # #print(info['stu02'])
# # print('stu03' in info) # info.has_key('stu03') in py2.x
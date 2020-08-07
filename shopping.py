print(__file__)
product_list=[
    ('IPhone',5600),
    ('Mac pro',9800),
    ('Bike',800),
    ('Watch',10800),
    ('Coofee',26),
    ('Python',89)
]
shoppig_list=[]
salary = input("input your Salary:")
print(("you salary is:\033[31;0m%s\033[1m") %(salary))
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choic=input("选择要购买的商品编号：>>>")
        if user_choic.isdigit():
            user_choic  = int(user_choic)
            if user_choic < len(product_list) and user_choic >= 0:
                p_item = product_list[user_choic]
                if p_item[1] <= salary: #买得起
                    shoppig_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into your shopping cart,you balance is \033[31;1m %s \033[0m " %(p_item,salary))
                else :
                    print("\033[41;1m你的余额只剩%s，还买个毛线啊！\033[0m" %salary)
            else:
                print("Product is not exist...")
        elif user_choic == 'q':
            print("---------shopping list---------")
            for p in shoppig_list:
                print(p)
            print("Your account is \033[32;1m %s \033[0m" %salary)
            exit()
            print("exit...")
        else:
            print("Invalid num")
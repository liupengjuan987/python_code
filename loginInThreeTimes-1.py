# f = open(r'D:\homework\namepasswd.xls','r', encoding='utf-8')
# f.read()
# print(f)
import pandas as pd
df = pd.read_excel(r'D:\homework\namepasswd.xlsx')
print(type(df))
print(df.shape)
# for index, row in df.iterrows():
#     row = dict(row)
#     name = row.get('name', '')
#     password = row.get('password', '')
#     print(name, password)
for i in range(3):
    username = input("username:")
    passwd = input("password:")
    for index, row in df.iterrows():
        row = dict(row)
        name = row.get('name', '')
        password = row.get('password', '')
        print(name,username)
        print(password,passwd)
        if name == username and password == passwd:
            print("Welcome user:{username}".format(username=name))
            break
        else:
            print("Invalid name or password!")
else:
    print("The account is locked!")
    file = open("name.txt", "a+")
    file.write(username)
    file.write("\n")
    file.close()


    #print(name,password)

# series = df.iloc[0]
# print(dict(series))
# for i in range (3):
#     username=input("username:")
#     passwd=input("password:")
#     if name== username and password ==passwd:
#         print("Welcome user:{username}".format(username=name))
#         break
#     else:
#         print("Invalid name or password!")
#         file = open("name.txt","a+")
#         file.write(name)
#         file.write("\n")
#         file.close()
# else:
#     print("The account is locked!")



name = "songsa \t love {name},{forever} years!"
print(name.capitalize())
print(name.count("s"))
print(name.center(50,"*"))#50长度 不够的*补
print(name.endswith("sa"))
print(name.expandtabs(tabsize=15))
print(name.find("g"))
print(name[name.find("love"):])
print(name.format(name='liupj',forever="forever"))
print(name.format_map({'name':'LiuPengjuan','forever':'forever'}))
print("asd123".isalnum()) #True
print("abCD".isalpha()) #True
print('1.23'.isdecimal()) #false
print('1A'.isdecimal()) #false
print('1A'.isdigit()) #false
print('_ 1A'.isidentifier()) #是否是合法标识符
print('22'.isnumeric()) #是否是数字
print('My Name Is'.istitle()) #是否首字母大写
print('My Name Is'.isprintable()) #tty drive file 基本不能打印
print('MY NAMW '.isupper())
print("+".join(['1','2','3']))
print(name.ljust(50,"*"))#左边50个字符 不够的*补齐
print(name.rjust(50,"*"))#右边50个字符 不够的*补齐
print(" So ng Sa ".strip())
print('*****')
print("\n Song Sa \n".lstrip())
print("Song Sa \n".rstrip())
print('*****')
p = str.maketrans("123456","abcdef")
print("521song".translate(p))
print("-------------")
print("songsa".replace("s","S",1))
print("SongSa".rfind("S"))#返回最右边一个所在下标
print('1+2+\n3+3'.splitlines())
print('SongSa'.swapcase())#交换大小写
print("song sa".title())#首字母大写
print("Songsa".zfill(30))

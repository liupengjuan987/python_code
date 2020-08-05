f = open("D:\homework\ptest.txt","r",encoding="utf-8")
f_new = open("D:\homework\ptest_2.txt","w",encoding="utf-8")

for line in f:
    if "lpj" in line:
        line = line.replace("lpj","LiuPengjuan")
    f_new.write(line)
f.close()
f_new.close()
nick = "liuengjuan"
def change_name(name):
    print("before change",name)
    global nick
    nick = name
    name = "Songss"
    print("after change",name)

name = "songsa"
print(nick)
print("****")
change_name(name)
print(name)
print(nick)
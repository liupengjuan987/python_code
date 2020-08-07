import getpass
_name="songsa"
_passwd="321521"
name=input("name:")
#passwd=getpass.getpass("passwd:")
passwd=input("passwd:")
if _name == name and _passwd == passwd:
    print("Welcome user {username} login".format(username=name))
else:
    print("Invalid name or passwd")
#print(name,passwd)
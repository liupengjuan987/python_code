name = input("name:")
age = input("age:")
#print(type(age), type(str(name)))
salary = input("salary:")  # salary=raw_input("salary:") py2 == py3
info = '''
   ****info of girl''' + name + ''''****
name:''' + name + '''
age:''' + age + '''
salary:''' + salary + '''
'''
info2 = '''
   ****info of girl %s****
name:%s
age:%s
salary:%s
''' % (name, name, age, salary)

info3 = '''
   ****info of girl {_name}****
name:{_name}
age:{_age}
salary:{_salary}
'''.format(
    _name=name,
    _age=age,
    _salary=salary
)
info4 = '''
   ****info of girl {0}****
name:{0}
age:{1}
salary:{2}
'''.format(name,age,salary)
print(info4)

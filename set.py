list = [1,5,7,9,6,7]
list_1 = set(list)
#print(list_1,type(list))

list2 = set([1,45,3,0,6,8,9])
#print(list2)
print(list2)
list2.add(521)#增一个
list2.update([0,888,666])#增多个
list2.remove(521)
print(list2.pop())#返回删掉的数字（随机删）
print(list2)
#print(list2.remove(521))#remove不存在会报错
print(list2.discard(521)) #不存在None
# print(list_1 & list2)#交集
# print(list_1 | list2)#并集
# print(list_1 - list2)#差集
# print(list_1 ^ list2)#对称差集：并集-交集

# inter = list_1.intersection(list2)#交集
# print(inter)
# print(list_1.union(list2))#并集
# print(list_1.difference(list2))#差集
# print(list2.difference(list_1))#差集
# print(list_1.issubset(list2))#子集
# print(list_1.issuperset(list2))#父集
# print(list_1.symmetric_difference(list2))#对称差集：并集-交集
# list3 = set([2,4,8])
# print(list_1.isdisjoint(list3))#是否有交集


from pip._vendor.distlib.compat import raw_input
x="a"
y="b"
if True:
    print(x),
    # raw_input("按下 enter 键退出，其他任意键显示...\n")
    print(y),
else:
    print("False")

# 变量赋值
a=1
b="2"
c=3.0
e=f=g=5
h=i=j=7,8.0,9
k,l,m=11,12,13

# del b #del  测试
# print(a);print(b);print(c)
# print(e);print(f);print(g);print(h);print(i);print(j)
# print (k,l,m)
# print ("你好，世界")
# #字符串 *  +
# print('--------')
# s = 'abcdef'
# hh='等等'
# print(s[1:6]) #字符串截取
# print(s*2)    #字符串 *
# print(hh+s)   #字符串 +

# numList = [1, 2, 3]
# for i in numList:
#     for each in i:
#         each=="n"
#          #   index=i.index()
#         print(each)
#     print(i+"--"+j)
# li = ['a', 'b', 'new', 'D', 'b', 'example', 'new', 'two', 'elements']
# print (li.index("example"))
# print (li.index("new"))
# print (li.index("b"))
# print ("c" in li)


# a = ["a","b","c","d","e","f"]
# for i,j in enumerate(a):
#     print (i,j)

#--------------数据类型-----------------
def typeClass():
    x = 10
    print(type(x))

    # x =  ["apple", "banana", "cherry"]
    # y =  ("apple", "banana", "cherry")
    # z =  range(6)
    # print(type(x))
    # print(type(y))
    # print(type(z))

#--------------列表/元组、range----------------------
    list1 = ['Google', 'Runoob', 1997, 2000]
    list2 = [1, 2, 3, 4, 5, 6, 7]

    print("list1[0]: ", list1[0])
    print("list2[1:5]: ", list2[1:5:2])
    print("list2[1:5]: ", list2[-1::-2])

    tu=(1, 2, 3, 4, 5, 6, 7)
    # print(tu[1:6:2])
    # for i in range(0,6):
    #     print(i)

    s = [1, 2, 3, 4, 1, 1]
    s = [i for i in s if i != 1]
    print(s)

    a = "woshishazi\n!!!"
    a = a.replace('\n', '')
    print(a)
# --------------集合set, frozenset----------------------
    set1=set()
    for i in range(0,6):
        set1.add(i)
    print(set1)
    set1.update('dddacvcd')
    set1.add('dddacvcd')
    set1.union({10,1})
    # print(set1)

typeClass()



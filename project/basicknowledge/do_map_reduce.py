from functools import reduce
## 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name.capitalize()
# test
list1 = ['adam', 'LISA', 'barT']
list2 = list(map(normalize, list1))
print(list2)


def prod(list):
     return reduce(lambda x, y: x * y, list)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('success!')
else:
    print('fail!')

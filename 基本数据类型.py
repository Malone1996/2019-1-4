# print("I'm z")
# movie_name=input('请输入一个电影名称:')
# print('你要的' + movie_name +'的下载地址为:http://www.baidu.com')
# print(f'你要的{movie_name}的下载地址为:http://www.baidu.com')
a = 10
b = 3.14
c = True
d = 'a'
print(type(a))
print(type(b))
print(type(c))
print(type(d))
# list列表，类似于c的array
# 1.创建列表 列表中尽量存放同一类型的东西
a = []
a = list()
a = ['zhangsan', 'lisi', 'wangwu']
a = [10, 'zhangsan', 3.14, True]
# 2.向列表添加元素
# insert 插入
# 参数1 index 索引，就是数字，一般从0开始
# 参数2 object 对象，Python里所有东西都属于对象

# append 追加
a.insert(0, 40)  # 将40这个对象插入第0个位置
a.insert(3, 60)  # 将60这个对象插入第3个位置（位置从0开始）
a.append(100)  # 追加到末尾
print(a)

citys = []
citys.append('郑州')
citys.append('北京')
citys.append('北京')
citys.append('广州')

print(citys)
citys.remove('北京')
print(citys)
citys.pop(2)
print(citys)

# 3.删除
# remove 移除符合条件的 第一个 对象
# pop 通过索引值删除对象,索引值从0开始

# 4.修改 不是用.调用方法
citys[1] = '上海'  # 将索引值为1的修改为上海
print(citys)

# 5.查找
print('北京' in citys)  # 判断北京是否在列表里,返回布尔值
print('上海' in citys)  # 判断上海是否在列表里,返回布尔值

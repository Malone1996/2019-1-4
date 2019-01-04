# 练习
# 1.创建一个空列表 imgs
# 2.利用for循环向列表中追加10个元素,分别是001.jpg,002.jpg...
# 3.从列表中获取一个名称并下载(用print代替)
# 4.下载成功后将其删除

# 自己代码
# imgs = []
# for i in range(1, 11):
#     imgs.append(f'{i}.jpg')
# print(imgs)
# tem = input('请输入要下载的图片:')
# imgs.remove(tem)
# print(imgs)
# print('下载成功')


# 老师代码
imgs = []
for i in range(1, 11):
    imgs.append(f'00{i}.jpg')

img_name = imgs[0]
print(f'{img_name}下载成功')
imgs.pop(0)

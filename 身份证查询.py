import requests
import json

ID = input('请输入要查询的身份证:')
print('正在查询...')
f = open("F:/data.txt", 'a+')
url = f'http://api.k780.com:88/?app=idcard.get&idcard={ID}&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json'
content = requests.get(url).text
data = json.loads(content)
data1 = data['result']
print('查询结果如下')

print('身份证号:', data1['idcard'])
text1 = data1['idcard']
f.write('身份证号:')
f.write(text1)
f.write('\n')

print('出生日期:', data1['born'])
text2 = data1['born']
f.write('出生日期:')
f.write(text2)
f.write('\n')

print('性别:', data1['sex'])
text3 = data1['sex']
f.write('性别:')
f.write(text3)
f.write('\n')

print('区号:', data1['areano'])
text4 = data1['areano']
f.write('区号:')
f.write(text4)
f.write('\n')

print('地区:', data1['style_citynm'])
text5 = data1['style_citynm']
f.write('地区:')
f.write(text5)
f.write('\n')
f.write('---------------------------------------------------')
f.write('\n')
f.close()

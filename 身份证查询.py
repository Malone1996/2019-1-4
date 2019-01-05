import requests
import json

ID = input('请输入要查询的身份证:')
print('正在查询...')
url = f'http://api.k780.com:88/?app=idcard.get&idcard={ID}&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json'
content = requests.get(url).text
data = json.loads(content)
data1 = data['result']
print('查询结果如下')
print('身份证号:', data1['idcard'])
print('出生日期:', data1['born'])
print('性别:', data1['sex'])
print('区号:', data1['areano'])
print('地区:', data1['style_citynm'])


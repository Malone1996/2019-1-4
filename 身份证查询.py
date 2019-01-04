import requests

ID = input('请输入要查询的身份证:')
url = f'http://api.k780.com:88/?app=idcard.get&idcard={ID}&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json'
content = requests.get(url).text
print(content)

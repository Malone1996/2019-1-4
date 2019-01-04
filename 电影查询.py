import requests

print('热门电影查询')
city = input('请输入要查询的地区:')
url = f'http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location={city}&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'
content = requests.get(url).text
print(content)

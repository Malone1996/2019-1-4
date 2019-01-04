import urllib.request  # ctrl+alt+l代码格式整理

for a in range(1, 11):
    url = f'http://www.ivsky.com/tupian/index_{a}.html'
    url_path = f'{a}.html'
    urllib.request.urlretrieve(url, url_path)
    print(f'{a}下载成功')

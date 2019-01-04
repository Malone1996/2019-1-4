# 目标:下载网页内的所有图片
# 1.需要获取图片的src name
# 2.图片的相关信息存放于网页中
# 3.下载网页


import requests  # 获取网页源码
from lxml import etree
import urllib.request

for a in range(10):
    url = f'http://www.ivsky.com/tupian/ziranfengjing_t2800/index_{a}.html'
    # 参数1 url,网址
    # 参数2 params,其他参数,默认为None
    content = requests.get(url).text
    root = etree.HTML(content)

    imgs = root.xpath('//img/@src')  # 找img标签下的src
    for i in range(18):
        urllib.request.urlretrieve(imgs[i], f'00{a}{i + 1}缩略图.jpg')  # 两个参数,一个地址,一个保存文件名
        # urllib.request.urlretrieve(imgs[i].replace('/t/', '/pre/'), f'00{a}{i + 1}高清图.jpg')  # 两个参数,一个地址,一个保存文件名
        # 字符串 替换
        # 高清图:http: // img.ivsky.com / img / tupian / pre / 201807 / 06 / bangwan_caiyun.jpg
        # 缩略图:http: // img.ivsky.com / img / tupian / t / 201807 / 06 / bangwan_caiyun.jpg

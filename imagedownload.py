import urllib.request

image_src="http://win.web.ri03.sycdn.kuwo.cn/ab06db48d772e3232a5b66175f3252ba/5c2ecef8/resource/a2/17/18/3412629003.aac"
image_path="消愁.aac"
urllib.request.urlretrieve(image_src, image_path)
print("下载成功")
from io import BytesIO
import requests
import easyocr

f = BytesIO()

try:
    res = requests.get(url="http://baotou2023.oss-cn-hangzhou.aliyuncs.com/0005a81c64af11ee9a000242ac120003.jpg",
                       timeout=5)
except Exception as exc:
    raise RuntimeError("微信auth.getAccessToken接口网络连接错误") from exc

if res.status_code == 200:
    f.write(res.content)

# 创建reader对象
reader = easyocr.Reader(['ch_sim', 'en'])
# 读取图像
result = reader.readtext("http://xuzhou2023.oss-cn-hangzhou.aliyuncs.com/files/000040ac642311eebcdd0242ac150003.jpg")

print(result)

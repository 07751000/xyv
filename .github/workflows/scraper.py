import requests
from bs4 import BeautifulSoup

# 请求页面
url = "http://tonkiang.us/hoteliptv.php"
response = requests.get(url)
response.encoding = 'utf-8'

# 解析HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 查找Hotel IPTV栏目下的酒店源IP地址的频道信息
channels = []

for item in soup.find_all('li'):  # 假设频道信息在li标签中
    channel_info = item.get_text(strip=True)
    if "IP地址" in channel_info:  # 根据关键字筛选
        channels.append(channel_info)

# 将有效的频道信息写入TXT文件
with open('channels.txt', 'w', encoding='utf-8') as f:
    for channel in channels:
        f.write(f"{channel}\n")

print("频道信息已成功写入channels.txt文件")

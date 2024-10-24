import requests
import re

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:BANDWIDTH=1755600,RESOLUTION=1280x720,CODECS="avc1.64001f,mp4a.40.2"')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "Referer": "https://embed.vindral.com/?core.channelId=alteregomedia_megatv1_ci_6cc490c7-e5c6-486b-acf0-9bb9c20fa670"
}

url = "https://embed.vindral.com/?core.channelId=alteregomedia_megatv1_ci_6cc490c7-e5c6-486b-acf0-9bb9c20fa670"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    site_content = response.text
    match = re.search(r'data-jwt="(.*?)"', site_content)
    
    if match:
        data_jwt_value = match.group(1)
        live_url_main = f"https://www.megatv.com/live/{data_jwt_value}/live/2/0/index.m3u8"
        print(live_url_main)
    else:
        print("https://Live URL not found in the content.")
else:
    print("https://Failed to fetch the website content.")

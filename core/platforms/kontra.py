
import requests
from bs4 import BeautifulSoup
import re

# URL of the webpage containing the wmsAuthSign
webpage_url = 'https://live24.gr/webtv/kontrachannel/'

# Fetch the content of the webpage
response = requests.get(webpage_url)
if response.status_code == 200:
    webpage_content = response.text
else:
    raise Exception(f"Failed to fetch the webpage: {webpage_url}")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(webpage_content, 'html.parser')

# Find the wmsAuthSign in the HTML content
wmsAuthSign = None
for script in soup.find_all('script'):
    if 'wmsAuthSign' in script.text:
        # Extract the wmsAuthSign from the script text
        match = re.search(r'wmsAuthSign=([a-zA-Z0-9%_-]+)', script.text)
        if match:
            wmsAuthSign = match.group(1)
            break

if not wmsAuthSign:
    raise Exception("wmsAuthSign not found in the webpage")

# Construct the final m3u8 URL with the wmsAuthSign
m3u8_base_url = 'https://kontralive.siliconweb.com/live/kontratv/playlist.m3u8'
final_m3u8_url = f"{m3u8_base_url}?wmsAuthSign={wmsAuthSign}"
# Fetch the m3u8 content from the final URL
m3u8_response = requests.get(final_m3u8_url)
if m3u8_response.status_code == 200:
    m3u8_content = m3u8_response.text
else:
    raise Exception(f"Failed to fetch the m3u8 file {final_m3u8_url}")

# Save the m3u8 content to a file
with open('kontra.m3u8', 'w') as file:
    file.write(m3u8_content)

print(f"The final m3u8 URL is {final_m3u8_url}")
print("The m3u8 content has been saved to kontra.m3u8")

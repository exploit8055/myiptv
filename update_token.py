import re
import requests

M3U8_FILE = "myiptv.m3u8"  # Replace with the actual filename in your repo
TOKEN_URL = "https://api.npoint.io/be2f8f200b5bb9130bdb"

response = requests.get(TOKEN_URL)
token = response.json().get("token")

if not token:
    raise Exception("No token found.")

with open(M3U8_FILE, "r", encoding="utf-8") as f:
    content = f.read()

pattern = r'(#EXTHTTP:\{"Authorization":"Bearer )[^"]+("\})'
replacement = rf'\1{token[7:]}\2'  # strip "Bearer " prefix

new_content = re.sub(pattern, replacement, content)

if new_content != content:
    with open(M3U8_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Token updated.")
else:
    print("No changes needed.")


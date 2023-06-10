'''
import requests
URL = "https://cdn33.armdb.org/file/armdb-hls/videos/51195/p_1_23.ts"
response = requests.get(URL)
open("instagram.ico", "wb").write(response.content)
'''
import requests

print(requests.__version__)

url = "https://cdn33.armdb.org/file/armdb-hls/videos/51195/p_1_01.ts"

'''
headers = {
    "Remote-Address": "51.195.100.55:443",
    "Origin": "null",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}
'''

headers = {
    "Remote-Address": "51.77.193.37:443",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en,en-US;q=0.9,ja-JP;q=0.8,ja;q=0.7,ru-RU;q=0.6,ru;q=0.5,hy-AM;q=0.4,hy;q=0.3",
    "Connection": "keep-alive",
    "Host": "cdn12.armdb.org",
    "Origin": "null",
    "Referer": "https://armdb.org/",
    "sec-ch-ua": "Google Chrome;v=107, Chromium;v=107, Not=A?Brand;v=24",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Linux",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

#response = requests.get(url, headers=headers)
response = requests.get(url, headers=headers, cert="/home/user/mytv/cert.pem", verify=False, ca_bundle="./cert.pem")

if response.status_code == 200:
    # Save the file to disk
    open("file.ts", "wb").write(response.content)
    print("File downloaded successfully")
else:
    print("Failed to download file")


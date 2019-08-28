import requests

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
url="https://m801.music.126.net/20190828180052/1403a610d0eaedbfb364f87d177df799/jdyyaac/030b/520e/5653/4a57db6393ed114add19a91585cf0185.m4a"
miFeng=requests.get(url,headers=headers,stream=True)

with open("./song/蜜蜂.mp3",'wb')as file:
    for i in miFeng.iter_content(10240):
        file.write(i)
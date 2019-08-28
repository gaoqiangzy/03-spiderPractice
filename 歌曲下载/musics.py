import requests,re
from bs4 import BeautifulSoup

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "Referer":"https://music.163.com"
}

def getInfo():
    url = "https://music.163.com/playlist?id=2342010207"
    base_url = "https://link.hhtjim.com/163/"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")

    # 1. 获取歌曲列表根标签ul
    ul = soup.find('ul', attrs={"class": "f-hide"})
    # 2. 获取ul下的所有li
    li = ul.children
    # 3.遍历li,获取所有的href和歌曲名
    songs = []
    for i in li:
        href = i.a.attrs["href"] + ".mp3"
        name = i.a.text
        true_href = href.strip("/song?id=")
        songs.append({"name": name, "href": base_url + true_href,"headers":headers})
    return songs

def downLoadSongs(songs):
    for song in songs:
        https=song["href"]
        name=song["name"]
        headers=song["headers"]

        try:
            song_r=requests.get(https,headers,stream=True)
            with open("./songs/%s.mp3"%(name),"wb") as file:
                for i in song_r.iter_content(10240):
                    file.write(i)
            print(f"{name}下载成功")
        except Exception as e:
            print(e)

songs=getInfo()
downLoadSongs(songs)




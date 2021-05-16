import random
import requests
from bs4 import BeautifulSoup

link="https://jbzd.com.pl/"

def find_img(link):
    result=requests.get(link)
    src=result.content
    soup=BeautifulSoup(src, 'lxml')
    imgs=[]
    for img in soup.find_all("img", "article-image"):
        imgs.append(img.attrs['src'])
    return imgs[random.randint(0, len(imgs)-1)]
meme=requests.get(find_img(link), allow_redirects=True)
open('meme.jpg', 'wb').write(meme.content)
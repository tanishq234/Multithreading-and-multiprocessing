'''
https://unsplash.com/
https://unsplash.com/illustrations
https://unsplash.com/plus/new
'''

import threading
import requests

from bs4 import BeautifulSoup

urls=[
    'https://unsplash.com/',
'https://unsplash.com/illustrations',
'https://unsplash.com/plus/new'
]

def fetch_contents(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {(len(soup.text))}chararcters from {url}')
    
threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
print("all web pages fetched")    
    
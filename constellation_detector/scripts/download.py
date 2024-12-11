import os
import urllib.request


def download(url, save_path):
    with urllib.request.urlopen(url) as web_file:
        with open(os.path.join(save_path, url.split('/')[-1]), 'wb') as local_file:
            local_file.write(web_file.read())

with open('txt.txt', 'r', encoding='utf-8') as f:
    links = [_.strip() for _ in f.readlines()]

for link in links:
    download(link, 'downloaded')
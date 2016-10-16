import requests
from bs4 import BeautifulSoup
import time


def output(wordListURL):
    req = requests.get(wordListURL, headers=headers)
    bsObj = BeautifulSoup(req.text)
    for tag in bsObj.find_all("strong"):
        explanation = tag.parent.next_sibling.next_sibling.string
        explanation = explanation.replace('\n', '') #delete "\n" in html
        f.write(tag.string + ",\"" + explanation + "\"\n")

f = open('result.csv', 'a')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}

wordBook = 'https://www.shanbay.com/wordbook/81361/'
req = requests.get(wordBook, headers=headers)
bsObj = BeautifulSoup(req.text)
wordListsPages = []
for tag in bsObj.find_all(class_="wordbook-wordlist-name"):
    wordListsPages.append(tag.a.get('href'))

# concatenate the URLs
wordListsURLs = []
for wordLists in wordListsPages:
    wordListsURLs.append("http://www.shanbay.com" + wordLists)

for wordListsURL in wordListsURLs:
    for page in range(7):
        output(wordListsURL + "?page=" + str(page + 1))
        time.sleep(1)

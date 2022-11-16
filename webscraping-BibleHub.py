import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request



webpage = 'https://ebible.org/asv/JHN'

J_chap = random.randint(1,21)

if J_chap < 10:
    J_chap = '0' + str(J_chap)
else:
    J_chap = str(J_chap)

webpage = 'https://ebible.org/asv/JHN' + J_chap + '.htm'

print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

bible_verses = soup.findAll('div',class_='main')


#print(bible_verses)

for verse in bible_verses:
    verse_list = verse.text.split('.')

#print(verse_list)

my_verse = random.choice(verse_list[:len(verse_list)-5])

#print(f"Chapter: {J_chap} , Verse: {my_verse}")

message = "Chapter: " + J_chap + " Verse: " + my_verse

print(message)

#Twilio stuff but I didn't do this
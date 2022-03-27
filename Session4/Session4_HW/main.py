import requests
from bs4 import BeautifulSoup

from webtoon import extract_info



file = open('webtoon.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(['title','author','rating'])


Webtoon_URL = f'https://comic.naver.com/webtoon/weekdayList?week=thu'
webtoon_html = requests.get(Webtoon_URL)
webtoon_soup = BeautifulSoup(webtoon_html.text,"html.parser")

webtoon_img_list = webtoon_soup.find("ul",{"class":"img_list"})
webtoon_list = webtoon_img_list.find_all("li")


final_result = []
final_result += extract_info(webtoon_list)

for i in final_result:
    row = []
    row.append(i['title'])
    row.append(i['author'])
    row.append(i['rating'])
    writer.writerow(row)

print(final_result)
import requests
from bs4 import BeautifulSoup

WEBTOON_URL = f'https://comic.naver.com/webtoon/weekdayList?week=sun'
webtoon_html = requests.get(WEBTOON_URL)
webtoon_soup = BeautifulSoup(webtoon_html.text,"html.parser")
print(webtoon_soup)

webtoon_list_box = webtoon_soup.find("ul",{"class":"img_list"})
webtoon_list = webtoon_list_box.find_all("li")

def extract_info(webtoon_list):
    result = []
    
    for webtoon in webtoon_list:
        title = webtoon.find("dl").find("a").string
        author = webtoon.find("dd",{"class":"desc"}).find("a").string
        rating = webtoon.find("div",{"class":"rating_type"}).find("strong").string
        webtoon_info = {
            'title' : title,
            'author' : author,
            'rating' : rating
        }
        result.append(webtoon_info)
    print(result)

 


# title = webtoon_list.find("dl").find("a").string


# print(title)
# # dl ->dt->a 
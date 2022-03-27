def extract_info(egg_list):
    result = []

    for egg in egg_list:
        title = egg.find("div",{"class":"basicList_title__3P9Q7"}).find("a").string
        price = egg.find("div",{"class":"basicList_price_area__1UXXR"}).find("span",{"class":"price_num__2WUXn"}).text
        detail_lists = egg.find("div",{"class":"basicList_detail_box__3ta3h"}).find_all("a")
        
        detail = []
        for list in detail_lists:
            detail.append(list.text)

        egg_info = {
            'title': title,
            'price': price,
            'detail': detail,
        }
        result.append(egg_info)
    return result











# result = {
#     'title': title,
#     'price': price,
#     'detail': detail_lists,
# }

# print(result)

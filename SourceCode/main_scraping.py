from bs4 import BeautifulSoup # BeautifulSoup in bs4 package
import requests
import csv
import json
import codecs

# 12384
for page_number in range(5547, 8001):
    # the main page URL
    # get the soup of page with number

    URL = 'https://hoidap.thuvienphapluat.vn/tim-theo-tu-van.html?page=' + str(page_number)
    try:
        get_page = requests.get(URL, timeout=10)
        soup = BeautifulSoup(get_page.text, 'lxml')
        print(page_number)
        #get the title of element
        parent_element = soup.find_all('div', class_='parent-item')
        for element in parent_element:
            #get each single link in this page of search question page
            link = 'https://hoidap.thuvienphapluat.vn' + str(element.a['href'])
            title = element.find('a', class_='tieu-de').h4.text
            get_page2=requests.get(link, timeout=10)
            soup2=BeautifulSoup(get_page2.text,'lxml')
            div_answer = soup2.find_all('div', class_='cautraloi')
            # print(title)
            for p_ans in div_answer:
                # print(p_ans.text)
                dictionary={
                    "question":title,
                    "answer":p_ans.text
                }
                with codecs.open('D:\sample2.json', mode='a',encoding='utf-8') as f:
                    json_obj = json.dumps(dictionary, indent=4, ensure_ascii=False)
                    f.write(json_obj)
    except requests.exceptions.Timeout:
        get_page = requests.get(URL, timeout=10)
        soup = BeautifulSoup(get_page.text, 'lxml')
        print(page_number)
        # get the title of element
        parent_element = soup.find_all('div', class_='parent-item')
        for element in parent_element:
            # get each single link in this page of search question page
            link = 'https://hoidap.thuvienphapluat.vn' + str(element.a['href'])
            title = element.find('a', class_='tieu-de').h4.text
            get_page2 = requests.get(link, timeout=10)
            soup2 = BeautifulSoup(get_page2.text, 'lxml')
            div_answer = soup2.find_all('div', class_='cautraloi')
            # print(title)
            for p_ans in div_answer:
                # print(p_ans.text)
                dictionary = {
                    "question": title,
                    "answer": p_ans.text
                }
                with codecs.open('D:\sample2.json', mode='a', encoding='utf-8') as f:
                    json_obj = json.dumps(dictionary, indent=4, ensure_ascii=False)
                    f.write(json_obj)




        # with open('D:/scraping.csv', mode='a', newline='', encoding="utf-8") as f:
        #     fieldnames = ['title', 'link']
        #     f = csv.DictWriter(f, fieldnames=fieldnames) #, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
        #     f.writerow({'title': title, 'link': link})





# URL2 = 'https://hdpl.moj.gov.vn/Pages/chi-tiet-hoi-dap.aspx?lv=1'
# content2 = requests.get(URL2)
# soup2 = BeautifulSoup(content2.text, 'html.parser')
#
# tit = soup2.findAll('div', class_='title-viewdetail')
# links2 = [link.find('a').attrs["href"] for link in tit]
# print(links2)
#.gov fail because it is using the asp.net system, binding the original url by the id, hold the id show the original URL, but how can get the original URL

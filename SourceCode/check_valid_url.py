from bs4 import BeautifulSoup  # BeautifulSoup is in bs4 package
import requests
import csv


csv_columns = ['Question', 'Answer', 'Date-asked']
#write header for csv file:
with open('/home/ntp/Desktop/QA_law/lan1.csv', mode='w') as f_:
    writer = csv.DictWriter(f_, fieldnames=csv_columns)
    writer.writeheader()
f_.close()

# 12384
for page_number in range(1, 12384):
    URL = 'https://hoidap.thuvienphapluat.vn/tim-theo-tu-van.html?page=' + str(page_number)
    try:
        get_page = requests.get(URL, timeout=30)
        soup=BeautifulSoup(get_page.text, 'lxml')
        print(page_number)
        parent_element=soup.find_all('div', class_='parent-item')

        for element in parent_element:
            link = 'https://hoidap.thuvienphapluat.vn' + str(element.a['href'])
            get_page2 = requests.get(link, timeout=30)
            if(get_page2.status_code == 200):
                title = element.find('a', class_='tieu-de').h4.text
                soup2 = BeautifulSoup(get_page2.text, 'lxml')
                div_answer = soup2.find_all('div', class_='cautraloi')
                div_date_asked = element.find('span', class_='ngayhoi')
                for p_ans in div_answer:
                    with open('/home/ntp/Desktop/QA_law/lan1', mode='a', newline='', encoding='utf-8') as f:
                        f = csv.DictWriter(f, fieldnames=csv_columns)
                        f.writerow({'Question': title,
                                    'Answer': p_ans.text,
                                    'Date-asked':div_date_asked.text})

    except:
        get_page = requests.get(URL, timeout=30)
        soup=BeautifulSoup(get_page.text, 'lxml')
        print(page_number)
        parent_element=soup.find_all('div', class_='parent-item')

        for element in parent_element:
            link = 'https://hoidap.thuvienphapluat.vn' + str(element.a['href'])
            get_page2 = requests.get(link, timeout=30)
            if(get_page2.status_code == 200):
                title = element.find('a', class_='tieu-de').h4.text
                soup2 = BeautifulSoup(get_page2.text, 'lxml')
                div_answer = soup2.find_all('div', class_='cautraloi')
                div_date_asked = element.find('span', class_='ngayhoi')
                for p_ans in div_answer:
                    # print(title)
                    # print(p_ans.text)
                    # print(div_date_asked.text)
                    with open('/home/ntp/Desktop/QA_law/lan1', mode='a', newline='', encoding='utf-8') as f:
                        f = csv.DictWriter(f, fieldnames=csv_columns)
                        f.writerow({'Question': title,
                                    'Answer': p_ans.text,
                                    'Date-asked':div_date_asked.text})

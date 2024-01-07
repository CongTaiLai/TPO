import os
import random
import time

import requests
from bs4 import BeautifulSoup

global headers
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Cookie': 'ga=GA1.2.123407450.1682602926; MEIQIA_TRACK_ID=2P0naHo5tmVPGxSD5DS2Ei1GWxd; MEIQIA_VISIT_ID=2P0naLdAChOD3GXSzbCfukBWoNH; device_unique_new=ae5e9df35d0af2e77c745d8818bd8893; temp_user_id=7b7b4ce742ffa03f4eb40eadf0073a693559f76786685690ea70557e655693dda%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22temp_user_id%22%3Bi%3A1%3Bs%3A32%3A%2259ac3e2e47a02f671ccedd11d331154b%22%3B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2214211325%22%2C%22%24device_id%22%3A%22187c2f31d9517-0c727d145d5e6-4f6a1573-2621440-187c2f31d9654c%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22187c2f31d9517-0c727d145d5e6-4f6a1573-2621440-187c2f31d9654c%22%7D; cookie_id=73F7B159-B1DB-B372-1BE1-2269A4554C94; channel_system_fourth=%E7%9B%B4%E6%8E%A5%E8%AE%BF%E9%97%AE; sid=13118; channel_system_fp=98af72f9bbb8ac6c8af01c0749d97e3f; Hm_lvt_96e9f9b616f9a233e432dd7441caa3c6=1700576506,1701354759,1702547153,1702699512; PHPSESSID=7uprmcpr2hqr5jnitpoop5dp95; current_url=https%3A%2F%2Ftop.zhan.com%2Ftoefl%2Fspeak%2Falltpo66.html; Hm_lpvt_96e9f9b616f9a233e432dd7441caa3c6=1702881979',
    'Pragma': 'no-cache', 'Sec-Ch-Ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': 'macOS',

    'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}  # Do not change this, or response.text(results) might be different.

d = eval(open('read_indexes.txt', 'r').read()).keys()
l = []
for i in d:
    l.append(i)
print(l)


def craw(soup, i, r):
    db = []
    if i != r - 2 and i != r - 1:  # [article, question, choices 1~4, answer]
        # Paragraph indicator
        try:
            pointer = soup.find('img', {'id': 'ParagraphAr'}).findParent('span', {'class': 'phase'})
            soup.find('span', {'data-translation': pointer['data-translation']}).insert_before('❖')
        except Exception:
            pass

        # Article
        try:
            div = soup.find('div', {'class': 'article'})
            for i in div.find_all('br'):
                i.replace_with('\n')
            db.append(div.text.removeprefix('\n'))
        except Exception:
            db.append('')

        # Question
        try:
            db.append(soup.find('div', {'class': 'left text'}).get_text(strip=True))
        except Exception:
            db.append('')

        # Choices
        if soup.find_all('input', {'type': 'radio'}) != []:
            for btn in soup.find_all('input', {'type': 'radio'}):
                try:
                    db.append(btn.parent.find('label').get_text())
                except Exception:
                    db.append('')
        else:
            for choice in soup.find_all('p', {'class': 'ops sec'}):
                try:
                    db.append(choice.get_text(strip=True))
                except Exception:
                    db.append('')

        # Answer
        try:
            db.append(soup.find('div', {'class': 'left correctAnswer'}).get_text().removeprefix('正确答案：'))
        except Exception:
            db.append('')

        # save
        database.append(db)

    elif i == r - 2:  # [article, question, answer]
        # Paragraph indicator
        try:
            pointer = soup.find('img', {'id': 'ParagraphAr'}).findParent('span', {'class': 'phase'})
            soup.find('span', {'data-translation': pointer['data-translation']}).insert_before('❖')
        except Exception:
            pass

        # Article
        try:
            div = soup.find('div', {'class': 'article'})
            for i in div.find_all('br'):
                i.replace_with('\n')
            db.append(div.text.removeprefix('\n'))
        except Exception:
            db.append('')

        # Question
        try:
            db.append(soup.find('p', {'class': 'ops empis'}).get_text(strip=True))
        except Exception:
            db.append('')

        # Answer
        try:
            db.append(soup.find('div', {'class': 'left correctAnswer'}).get_text().removeprefix('正确答案：'))
        except Exception:
            db.append('')

        # save
        database.append(db)

    elif i == r - 1:  # [article, choices 1~6, answer]
        # Article
        try:
            div = soup.find('div', {'class': 'article'})
            for i in div.find_all('br'):
                i.replace_with('\n')
            db.append(div.text.removeprefix('\n'))
        except Exception:
            db.append('')

        # Choices
        try:
            ch = soup.find_all('p', {'class': 'ops dragsec'})
            for c in ch:
                try:
                    db.append(c.get_text(strip=True))
                except Exception:
                    pass
        except Exception:
            pass

        # Answer
        try:
            db.append(soup.find('div', {'class': 'left correctAnswer'}).get_text().removeprefix('正确答案：'))
        except Exception:
            db.append('')

        # save
        database.append(db)


while True:
    dic = eval(open('read_indexes.txt', 'r').read())

    if len(dic) == 0:
        break

    test = dic[l[0]]

    for task in test:
        print(task)

        if int(l[0]) <= 54:
            r = 14
        else:
            r = 10

        global database
        database = []

        for i in range(r):
            response = requests.get(f'https://top.zhan.com/toefl/read/practicereview-{task}-13-0-{i}.html',
                                    headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            craw(soup, i, r)
        time.sleep(random.randint(30, 50) * 0.1)

        with open(str(os.getcwd().replace('/scripts/reading', '') + '/downloaded_resources/Reading/TPO' + str(
                l[0]) + '_' + str(test.index(task) + 1) + '.txt'), 'w') as file:
            file.write(str(database))

    del dic[l[0]]
    del l[0]

    open('read_indexes.txt', 'w').write(str(dic))
    print('a')

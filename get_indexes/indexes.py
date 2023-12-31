import random
import time
import re

import requests
from bs4 import BeautifulSoup

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

exam_sections = ['read', 'listen', 'speak', 'write']

for e in exam_sections:
    database = {}  # long links
    with open(f'../get_contents/{e}_contents.txt', 'r') as file:
        short_links = eval(file.read())

    # responses structure of each exam section is not equal
    if e == 'speak' or e == 'write':
        """
        # Each TPO: 
        <div class="cssExerciseArea">
         -> <h2 class="cssBodyTit">Official X
         -> <...>
             -> ...
             -> <a class="cssCheckReport md_click sensors_maidian" ... target="_blank">
        """
        for sl in short_links:
            response = requests.get(sl, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")

            divs = soup.find_all('div', {'class': 'cssExerciseArea'})
            for i in divs:  # TPOs
                l = []
                for j in i.findChildren('a', {'class': 'cssCheckReport md_click sensors_maidian', 'target': '_blank'}):
                    l.append(j['href'])  # links to each subsection of a single test

                titles = i.findChildren('h2', {'class': 'cssBodyTit'})[0]
                database[re.findall(r'\d+', l[i].__str__())[1]] = l
                print(database)

            time.sleep(0.1 * random.randint(30, 50))
            print(short_links.index(sl))

        with open(f'{e}_indexes.txt', 'w') as file_write:
            file_write.write(str(database))

    elif e == 'listen':
        """
        <div class="cssExerciseArea">
         # Each TPO:
         -> <h2 class="cssBodyTit">Official X
         -> <div class="cssExeBody">
             -> ...
             -> <a class="md_click sensors_maidian cssReview" target="_blank">
        """
        for sl in short_links:
            response = requests.get(sl, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            outer_divs = soup.find('div', {'class': 'cssExerciseArea'})

            l = outer_divs.contents

            for i in range(1, len(l), 2):
                if l[i].name == 'h2':
                    if l[i + 2].name == 'div':
                        divs = BeautifulSoup(l[i + 2].__str__(), 'html.parser')
                        database[re.findall(r'\d+', l[i].__str__())[1]] = [i['href'] for i in divs.findChildren('a', {
                            'class': 'md_click sensors_maidian cssReview', 'target': '_blank'})]

            time.sleep(0.1 * random.randint(30, 50))
            print(short_links.index(sl))

        with open(f'{e}_indexes.txt', 'w') as file_write:
            file_write.write(str(database))

    elif e == 'read':
        """
        <div class="cssExerciseArea">
         # Each TPO:
         -> <h2 class="cssBodyTit">Official X
         -> <div class="cssExeBody">
             -> ...
             -> <a class="md_click cssReview sensors_maidian" target="_blank">
        """
        for sl in short_links:
            response = requests.get(sl, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            outer_divs = soup.find('div', {'class': 'cssExerciseArea'})
            l = outer_divs.contents

            for i in range(1, len(l), 2):
                if l[i].name == 'h2':
                    if l[i + 2].name == 'div':
                        divs = BeautifulSoup(l[i + 2].__str__(), 'html.parser')
                        database[re.findall(r'\d+', l[i].__str__())[1]] = [i['href'] for i in divs.findChildren('a', {
                            'class': 'md_click cssReview sensors_maidian', 'target': '_blank'})]

            time.sleep(0.1 * random.randint(30, 50))

            print(short_links.index(sl))

        with open(f'{e}_indexes.txt', 'w') as file_write:
            file_write.write(str(database))

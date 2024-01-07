import os
import re

l = os.listdir('/Users/Taylor/Desktop/TPO_Scrape/downloaded_resources/Reading')

w = open('read_indexes.txt', 'w')
w_db = {}
r = eval(open('read_indexes_backup.txt', 'r').read())

for i in l:
    dic = eval(open(str('/Users/Taylor/Desktop/TPO_Scrape/downloaded_resources/Reading/' + i)).read())
    for x in dic:
        if len(x[-1]) == 2:
            issue_test = re.findall(r'\d+', i)[0]
            issue_task = re.findall(r'\d+', i)[1]

            print(re.findall(r'\d+', i))

            w_db[issue_test] = r[issue_test]

w.write(str(w_db))

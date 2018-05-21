import urllib
import json
from bs4 import BeautifulSoup
from cities import urlgen
import time

for x in range(1, 999):
    try:
        web = urllib.urlopen(urlgen())
        soup = BeautifulSoup(web.read(), 'lxml')
        data = soup.find_all("script")[11].string
        ndata = str(data)
        ndata.split('\n')
        jdata = str([line for line in ndata.split('\n') if line.strip() !=
                     ''][0].replace('            var bbbDtmData = ', ''))
        data = json.loads(jdata)
        f = open('test.txt', 'a+')
        for x in data['search']['results']:

            f.write('{} \n'.format(x['businessName']))
        f.close()
        time.sleep(1)
    except:
        pass


'''
p = re.compile('var bbbDtmData = (.*?);')
m = p.match(data)
stocks = json.loads(m.groups()[0])

for stock in stocks:
    print stock
'''

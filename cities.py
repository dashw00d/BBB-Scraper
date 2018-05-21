import json
import random


def urlgen():
    rooturl = 'https://www.bbb.org/en/us/search?'
    data = json.load(open("cities.json"))
    lat = []
    longt = []
    for x in data:
        lat.append(x['latitude'])
    for x in data:
        longt.append(x['longitude'])

    tiedup = zip(lat, longt)
    choice = random.choice(tiedup)
    location = '&find_latlng={}%2C{}'.format(choice[0], choice[1])
    keyword = random.choice(
        ['find_text=Burglar+Alarm+Systems', 'find_text=home+security+system'])
    page = '&page={}'.format(random.randint(0, 9))
    sort = '&sort={}'.format(random.choice(['Relevance', 'Rating', 'Name']))
    cfilter = '&filter_category={}'.format(random.choice(
        ['60788-000', '10077-000', '60790-000', '10077-000', '']))
    finalurl = '{}{}{}{}{}{}'.format(
        rooturl, keyword, location, page, sort, cfilter)
    return finalurl

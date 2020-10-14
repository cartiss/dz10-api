import requests
from pprint import pprint

url = 'https://superheroapi.com/api/2619421814940190/search/'

list_hero = ['Thanos', 'Hulk', 'Captain America']
tmp_list = []
max = 0
a = []

# 1-й Вариант

# for hero in list_hero:
#    response = requests.get(url + hero)
#    intelligence = response.json()['results'][0]['powerstats']['intelligence']
#    tmp_dict = {'name': hero, 'intelligence': intelligence}
#    tmp_list.append(tmp_dict)

# конец 1-го варианта

# 2-й Вариант

class Hero:
    intelligence = 0
    def __init__(self, name):
        self.name = name

    def search_intelligence(self):
        response = requests.get(url + self.name)
        self.intelligence = response.json()['results'][0]['powerstats']['intelligence']

for hero in list_hero:
    new_hero = Hero(hero)
    new_hero.search_intelligence()
    tmp_dict = {'name': new_hero.name, 'intelligence': new_hero.intelligence}
    a.append(tmp_dict)

# конец 2-го варианта

for dict_ in a:
    if int(dict_['intelligence']) > max:
        max = int(dict_['intelligence'])

for item in a:
    if int(item['intelligence']) == max:
        print(item['name'] + ' = ' + item['intelligence'])

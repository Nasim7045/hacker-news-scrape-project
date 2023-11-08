import requests
from bs4 import BeautifulSoup
import pprint

#links to hacker news page 1 & 2 , this was a mini project you can keep adding more pages in super/combined variable

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

#for ex: res3 with page 3 link ......and so on
links = soup.select('.titleline > a') 
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline > a') 
subtext2 = soup2.select('.subtext')

#add links nd subtexts into one super variable

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_votes(hn)
 
pprint.pprint(create_custom_hn(mega_links, mega_subtext))

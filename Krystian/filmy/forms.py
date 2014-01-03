from filmy.models import Film

import feedparser
import datetime
import re

#const
ignore_file = "/usr/local/lib/python2.7/dist-packages/django/bin/Krystian/filmy/ignore_words.txt"
prev_n = 100

#re
#episode_re = re.compile("S[0-9]{1,2}E[0-9]{1,2}")
seed_re = re.compile("Seeds: ([0-9,]+)")
peer_re = re.compile("Peers: ([0-9,]+)")

#open feed
rss_url = "http://torrentz.eu/feed"
feed = feedparser.parse(rss_url)

#load torrents
parsed_torrents = []
for item in feed["items"]:
    torrent = {}
    
    try:
        torrent["url"] = item["link"]
        torrent["timestamp"] = int(datetime.datetime.strptime(item["published"][:-6], '%a, %d %b %Y %H:%M:%S').strftime("%s"))
        torrent["name"] = item["title"]
        torrent["seeds"] = int(seed_re.search(item["summary"]).group(1).replace(",", ""))
        torrent["peers"] = int(peer_re.search(item["summary"]).group(1).replace(",", ""))
        #torrent["episode"] = episode_re.search(item["title"])
    except:
        continue #this should be rewritten
    
    parsed_torrents.append(torrent) # list of dicts where every one has name, seeds, etc

#clean names
ignore_words = map(lambda x: re.compile(x.strip(), re.I), open(ignore_file, "r").readlines())
ignore_words.append(re.compile(r'^ *'))
ignore_words.append(re.compile(r' *$'))
ignore_words.append(re.compile(r' +'))

for torrent in parsed_torrents:
    name = torrent["name"]
    for i in ignore_words:
        name = i.sub(" ", name)
    torrent["clean name"] = name.lower()

#delete duplicates
unique_torrents = {}
for torrent in parsed_torrents:
    clean_name = torrent["clean name"]
    if clean_name in unique_torrents:
        if torrent["seeds"] > unique_torrents[clean_name]["seeds"]:
            unique_torrents[clean_name] = torrent
    else:
        unique_torrents[clean_name] = torrent
        
some_torrents = unique_torrents[10]
        
for film in some_torrents:
    
    t = Film(name=film["name"], url=film["url"], seeds=film["seeds"], peers=film["peers"], date=film["timestamp"])
    t.save()
              
# changes:  
# >> b5.name = 'New name'
# >> b5.save()
        
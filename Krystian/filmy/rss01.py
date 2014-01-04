# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:18:21 2013

@author: piotr
"""

import feedparser
import datetime
import re
import sqlite3

#const
ignore_file = "/media/Magazyn L/Python/Torrent_viewer/ignore_words.txt"
sqlite3_file = "/media/Magazyn L/Python/Torrent_viewer/torrents.db"
prev_n = 1000

#re
#episode_re = re.compile("S[0-9]{1,2}E[0-9]{1,2}")
seed_re = re.compile("Seeds: ([0-9,]+)")
peer_re = re.compile("Peers: ([0-9,]+)")

#open database
con = sqlite3.connect(sqlite3_file)
cur = con.cursor()

#open feed
rss_url = "http://torrentz.eu/feed"
feed = feedparser.parse(rss_url)

#load filters
#filters = map(lambda x: re.compile(x.strip(), re.I), open("filters.txt", "r").readlines())

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

    parsed_torrents.append(torrent)
#    for f in filters:
#        if f.search(torrent["name"]):
#            torrenty.append(torrent)
#            break

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

#add torrents to database
cur.execute('select DATE from torrenty order by DATE limit 1')
last_ts = int(cur.fetchone()[0])

##read n previous torrents
prev_n_torrents = {}
cur.execute('select * from torrenty order by DATE limit '+str(prev_n))
while True:
    torrent = cur.fetchone()
    
    if torrent == None:
        break
    
    cname, name, url, seed, peer, ts = torrent    
    
    prev_n_torrents[cname] = {"name":name, "clean name":cname, "url":url, "seeds":seed, "peers":peer, "timestamp":ts}

##choose torrents to add
input_torrents = []
for cname in unique_torrents:
    torrent = unique_torrents[cname]
    if torrent["timestamp"] < last_ts:
        continue
    
    if cname in prev_n_torrents:
        if not torrent["seeds"] > int(prev_n_torrents["seeds"]):
            continue
    
    input_torrents.append((torrent["clean name"], torrent["name"], torrent["url"], torrent["seeds"], torrent["peers"], torrent["timestamp"]))


##add torrents
cur.executemany("insert into torrenty values(?, ?, ?, ?, ?, ?)", input_torrents)

con.commit()
con.close() 
























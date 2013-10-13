import urllib2
import re

'''
portale = ["http://www.wp.pl", "http://www.onet.pl", "http://www.o2.pl", "http://www.interia.pl", "http://www.gazeta.pl"]

p = urllib2.urlopen(portale[0])
html = p.read()


linki = [ i[(i.find('"')+1):-1] for i in re.findall(r'href="https?://[^ ]*"', html, re.I) ]
'''
#wp_linki = [ i[(i.find('"')+1):-1] for i in re.findall(r'<link .*', html, re.I) ]


wp_rss = 'http://rss.wp.pl/s,informacje,index.html'

wp = urllib2.urlopen(wp_rss)
html = wp.read()

wp_linki = [ i[(i.find(' ')):-1].split()[2].lstrip('href=') for i in re.findall(r'<link.*rss.*', wp_html, re.I) ]


for i in wp_linki:
    print i

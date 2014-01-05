# Create your views here.
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

import sqlite3
#from django.db.models import Q
from filmy.models import Film, SearchForm

from django.utils import timezone

from django.views.decorators.cache import cache_page

@cache_page(60 * 60, cache="default")
def torrent(request):
    return render_to_response('filmy/torrent.html')


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


@cache_page(60 * 15, cache="default")
def search(request):
    search_phrase = ''
    
    if 's_ph' in request.COOKIES:
        search_phrase = request.COOKIES['s_ph']  
    
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            
            query = form.cleaned_data['query']
            
            q = query.split(' ')
            select = """SELECT name, seeds, peers, url FROM torrenty WHERE"""
            for i in q:
                select += """ name LIKE "%""" + str(i) + """%" OR"""
            select += """DER BY seeds DESC LIMIT 100"""

            #data = sql_select.filter(name__contains=query)[:10] # app name _ model class name
            conn = sqlite3.connect("/home/repo/Krystian/Krystian/torrents.db")
            try:
                cursor = conn.cursor()
                cursor.execute(select)
                #data = cursor.fetchall()
                data = dictfetchall(cursor)
            finally:
                conn.close()
            
            #send cookie
            response = render_to_response('filmy/output.html', {'data':data, 'form':form, 'search_phrase':query,})
            response.set_cookie('s_ph', query)
            
            return response
           # return render(request, 'filmy/output.html',
               #          {'data':data, 'form':form, 'search_phrase':search_phrase,})

    else:
        #invalid data
        form = SearchForm(initial={'query': search_phrase})
       
    return render(request, 'filmy/index.html', {'form':form}) #initial={'sth':'drhtv'} from cookie or none
    
    
@cache_page(60 * 15, cache="default")
def krystian(request):
    #data = Film.objects.raw("""SELECT * FROM filmy_film WHERE NAME LIKE "%dvdrip%" OR NAME LIKE "%hdtv%" OR NAME LIKE "%tvrip%" OR NAME LIKE "%brrip%" """)
    #data = Film.objects.get(Q(name__contains='dvdrip') | Q(name__contains='hdtv') | Q(name__contains='tvrip') | Q(name__contains='brrip'))[:5]
 
    conn = sqlite3.connect("/home/repo/Krystian/Krystian/torrents.db")
    try:
        cursor = conn.cursor()
        cursor.execute("""SELECT name, seeds, peers, url FROM torrenty WHERE name LIKE "%dvdrip%" OR name LIKE "%hdtv%" OR name LIKE "%tvrip%" OR name LIKE "%brrip%" ORDER BY seeds DESC LIMIT 100""")
        #data = cursor.fetchall()
        data = dictfetchall(cursor)
    finally:
        conn.close()    
     
    return render(request, 'filmy/krystian.html', {'data':data, })
    


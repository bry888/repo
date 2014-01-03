# Create your views here.
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.db.models import Q
from filmy.models import Film, SearchForm

from django.utils import timezone
#import memcache
#from django.views.decorators.cache import cache_page

#@cache_page(60 * 10)
def search(request):
    search_phrase = ''
    
    if 's_ph' in request.COOKIES:
        search_phrase = request.COOKIES['s_ph']
    
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            #send cookie
            query = form.cleaned_data['query']
            
            response = HttpResponse(query)
            response.set_cookie('s_ph', query)
            
            #data = Film.objects.raw('SELECT ID, NAME, SEEDS, PEERS, URL FROM filmy_film WHERE name LIKE "' + str(query) + '"')[:10]
            data = Film.objects.raw('SELECT * FROM filmy_film WHERE NAME IS "' + str(query) + '"')[:10]
            #data = sql_select.filter(name__contains=query)[:10] # app name _ model class name
            
            return render(request, 'filmy/output.html',
                         {'data':data, 'form':form, 'search_phrase':search_phrase,})

    else:
        #invalid data
        form = SearchForm()
       
    return render(request, 'filmy/index.html', {'form':form}) #initial={'sth':'drhtv'} from cookie or none
    
    
def krystian(request):
    #data = Film.objects.raw("""SELECT * FROM filmy_film WHERE NAME LIKE "%dvdrip%" OR NAME LIKE "%hdtv%" OR NAME LIKE "%tvrip%" OR NAME LIKE "%brrip%" """)
    data = Film.objects.get(Q(name__contains='dvdrip') | Q(name__contains='hdtv') | Q(name__contains='tvrip') | Q(name__contains='brrip'))[:5]
    
    return render(request, 'filmy/krystian.html', {'data':data, })
    


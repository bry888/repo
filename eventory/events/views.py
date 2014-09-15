# Create your views here.
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from events.models import AddEventForm

import sqlite3

from django.utils import timezone

#from django.views.decorators.cache import cache_page
#@cache_page(60 * 60, cache="default")

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def mainpage(request):
            
    select = """select TITLE,RAW_TEXT,START_TS,LOCATION,URL from RAW_TEXTS where IS_EVENT = 'True' order by START_TS desc"""

    conn = sqlite3.connect("/home/repo/eventory/eventory/events_main.db")
    try:
        cursor = conn.cursor()
        cursor.execute(select)
        #data = cursor.fetchall()
        data = dictfetchall(cursor)
    finally:
        conn.close()
    
    return render(request, 'events/mainpage.html', {'data':data,})
    
    
    
def add_event(request):
    
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        if form.is_valid():
            
            title = form.cleaned_data['title']
            date_time = form.cleaned_data['date_time']
            description = form.cleaned_data['description']
            location = form.cleaned_data['location']
            url = form.cleaned_data['url']
    
            #add to database
            conn = sqlite3.connect("/home/repo/eventory/eventory/events_main.db")
            try:
                cursor = conn.cursor()
                cursor.execute(select)
                #data = cursor.fetchall()
                data = dictfetchall(cursor)
            finally:
                conn.close()
    
            return HttpResponseRedirect('')

        #return render(request, 'events/add_event.html', {'form':form,})

    else:
        #invalid data
        form = AddEventForm()
       
    return render(request, 'events/add_event.html', {'form':form})


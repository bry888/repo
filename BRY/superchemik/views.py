# Create your views here.
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

#from django.db.models import Q
from superchemik.models import Comment, CommentForm, Page

from django.utils import timezone

#from django.views.decorators.cache import cache_page
#import json

def mainpage(request, page_id):
    page = get_object_or_404(Page, id=page_id)
     
    # >>> Blog.objects.values('id', 'name')
    # [{'id': 1, 'name': 'Beatles Blog'}] 
    pages = Page.objects.all()
    
    comments = Comment.objects.filter(page_num=page_id).order_by('-date')
    #prev_page = page.get_absolute_url_prev()
    #next_page = page.get_absolute_url_next()
    
    #j = '{"page_num": ' + page_id + '}'
    #this_page = json.loads(j)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            
            content = form.cleaned_data['content']
            name = form.cleaned_data['name']
            
            comment = Comment(name=name, date=timezone.now(), content=content, page_num=page)
            comment.save()
            
            #return render(request, 'superchemik/mainpage.html', {'form': form, 'pages': pages, #'prev_page': prev_page, 'next_page': next_page,
             #                                                    'comments': Comment.objects.filter(page_num=page_id).order_by('-date'),
              #                                                   'page': page})
            return HttpResponseRedirect('')
    else:
        #invalid data
        form = CommentForm()


    response = render(request, 'superchemik/mainpage.html', {'form': form, 'pages': pages, #'prev_page': prev_page, 'next_page': next_page,
                      'comments': comments, 'page': page, 'page_id': page_id,})
    
    #response = HttpResponse(json, mimetype='application/json')
    
    response.set_cookie('p_n', page_id)
    
    return response



def page_from_cookie(request):
    if 'p_n' in request.COOKIES:
        page_num = request.COOKIES['p_n']
    else:
        page_num = 1
    return page_num

#@cache_page(5 * 60, cache="default")
def comments(request):
    
    page_num=page_from_cookie(request)
    
    comments = Comment.objects.all().order_by('-date')
    return render(request, 'superchemik/comments.html', {'comments': comments, 'page_num': page_num, })

#@cache_page(1000 * 60, cache="default")
def info(request):
    
    page_num=page_from_cookie(request)
    
    return render(request, 'superchemik/info.html', {'page_num': page_num, })

'''
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            
            content = form.cleaned_data['content']
            name = form.cleaned_data['name']
            
            comment = Comment(name=name, date=timezone.now(), content=content)
            comment.save()
            
            response = HttpResponseRedirect('/superchemik/komentarze')
    else:
        #invalid data
        form = CommentForm()
       
    return render(request, 'superchemik/add_comment.html', {'form':form})
'''            
# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import Http500
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from main_app.models import User, Articles, ArticlesReadByUser, ArticlesToShow


class MainView(generic.ListView):
    template_name = 'main_app/main_view.html'
    context_object_name = 'list_of_best_articles'
    def get_queryset(self):
        return Articles.objects.order_by('-read_freq')[:30]

@login_required(login_url='/login/')
class UserArticlesView(generic.ListView):
    model = ArticlesToShow
    template_name = 'main_app/user_view.html'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        
        return Poll.objects.filter(
            pub_date__lte=timezone.now() #polls from future not displayed
        ).order_by('-pub_date')[:6]
        """
        return ArticlesToShow.objects.all()[:30]

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("user_view")
    else:
        # Show an error page
        return render(request, 'login.html')

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("main_view")

def register_view(request):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    if password == password2:
        if username not in User.objects.all():
            user = User.objects.create_user(username, password)
            user.save()
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("user_view")
            else:
                raise Http500
        else:
            return render(request, 'register.html', error2)
    else:
        return render(request, 'register.html', error1)


class ArticleDetailView(generic.DetailView):
    model = Articles
    template_name = 'main_app/article.html'
'''
@login_required(login_url='/login/')
def read(request, article_id):
    p = get_object_or_404(ArticlesToRead, pk=article_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

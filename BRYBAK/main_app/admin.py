from django.contrib import admin
from brybak_rss.models import User, Articles, ArticlesReadByUser

class ArticlesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('user',    {'fields': ['username']}),
        ('title',   {'fields': ['article_title']}),
        ('subtitle', {'fields': ['article_subtitle']}),
        ('read_time', {'fields': ['reading_time']}),
    ]
    list_display = ('user', 'title', 'subtitle', 'read_time')
    list_filter = ['read_time']

admin.site.register(Articles, ArticlesReadByUser, ArticlesAdmin)

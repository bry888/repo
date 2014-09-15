from django.contrib import admin
from superchemik.models import Comment, Page

class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('content',  {'fields': ['content']}),
        ('date',  {'fields': ['date']}),
        ('page_num', {'fields': ['page_num']}),
    ]    
    list_display = ('name', 'content', 'date', 'page_num')
    list_filter = ['date']
    search_fields = ['name']
    date_hierarchy = 'date'
    
class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('image_name', {'fields': ['image_name']}),
    ]
    list_display = ['image_name']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Page, PageAdmin)
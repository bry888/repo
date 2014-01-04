from django.contrib import admin
from filmy.models import Film

class FilmAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('url',  {'fields': ['url']}),
        ('seeds',  {'fields': ['seeds']}),
        ('peers',  {'fields': ['peers']}),
        ('date',  {'fields': ['date']}),
    ]    
    list_display = ('name', 'url', 'peers', 'seeds', 'date')
    list_filter = ['date']
    search_fields = ['name']
    date_hierarchy = 'date'

admin.site.register(Film, FilmAdmin)
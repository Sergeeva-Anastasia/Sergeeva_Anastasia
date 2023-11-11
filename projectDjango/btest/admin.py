from django.contrib import admin
from .models import Chanells

class BbAdmin(admin.ModelAdmin):
  list_display = ('title', 'content')
  list_display_links = ('title', 'content')
  search_fields = ('title', 'content')
  
admin.site.register(Chanells, BbAdmin)


from django.contrib import admin
from .models import TVShows
admin.site.register(TVShows)


from django.contrib import admin
from .models import Type
admin.site.register(Type)


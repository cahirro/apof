from django.contrib import admin
from menus.models import *

# Register your models here.

class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ('nazwa', )
#    search_fields = ('imie', 'nazwisko', )

admin.site.register(Restaurants, RestaurantsAdmin)

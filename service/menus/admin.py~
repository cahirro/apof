from django.contrib import admin
from menus.models import *

# Register your models here.
class HungryPeopleAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', )
    search_fields = ('imie', 'nazwisko', )

class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ('nazwa', )
#    search_fields = ('imie', 'nazwisko', )

admin.site.register(HungryPeople, HungryPeopleAdmin)
admin.site.register(Restaurants, RestaurantsAdmin)

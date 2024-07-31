from django.contrib import admin
from .models import mysolarrr

class solarAdmin(admin.ModelAdmin):
    list_display = ['Solar_generation','Daily_production','Monthly_sales']  # Fields to display in the list view
   

admin.site.register(mysolarrr, solarAdmin)

from django.contrib import admin
from .models import SolarData




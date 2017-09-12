from django.contrib import admin

from .models import Appliance, Room, Dwelling, ElectricityUsage

admin.site.register(Appliance)
admin.site.register(Room)
admin.site.register(Dwelling)
admin.site.register(ElectricityUsage)
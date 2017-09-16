from django.contrib import admin

from .models import Appliance, Room, Dwelling, ElectricityUsage, WaterUsage

admin.site.register(Appliance)
admin.site.register(Room)
admin.site.register(Dwelling)
admin.site.register(ElectricityUsage)
admin.site.register(WaterUsage)
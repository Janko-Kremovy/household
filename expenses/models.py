from django.db import models
from django.forms import ModelForm


# The home style (eg. house/apartment)
class Dwelling(models.Model):
    type = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.type + ' @ ' + self.address

    def save_dwelling(self, request):
        self.type = request.POST['type' + str(self.id)]
        self.address = request.POST['address' + str(self.id)]
        self.save()
        return True


# The room type (eg. laundry/kitchen/living room)
class Room(models.Model):
    dwelling = models.ForeignKey(Dwelling, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def save_room(self, request):
        self.name = request.POST['room_name' + str(self.id)]
        self.save()
        return True


# The appliance details (eg. Braun Dishwasher X 2015, uses electricity = true and uses water = true )
class Appliance(models.Model):
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    uses_electricity = models.BooleanField(default=False)
    uses_water = models.BooleanField(default=False)
    uses_gas = models.BooleanField(default=False)

    def __str__(self):
        return self.type

    def save_appliance(self, request):
        self.type = request.POST['appliance_type' + str(self.id)]
        self.make = request.POST['appliance_make' + str(self.id)]
        self.model = request.POST['appliance_model' + str(self.id)]
        self.year = int(request.POST['appliance_year' + str(self.id)])
        self.save()
        return True


class ElectricityUsage(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)
    watts = models.IntegerField()
    time_minutes = models.IntegerField()
    occurrences_per_week = models.IntegerField()

    def __str__(self):
        return str(self.time_minutes) + ' minutes @ ' + str(self.watts) + 'W, ' + str(self.occurrences_per_week) + ' times per week.'

    def set_watts(self, in_watts):
        if in_watts >= 0:
            self.watts = in_watts

    def save_electricity_usage(self, request):
        self.set_watts(int(request.POST['electricity_usage_watts' + str(self.id)]))
        self.time_minutes = int(request.POST['electricity_usage_time_minutes' + str(self.id)])
        self.occurrences_per_week = int(request.POST['electricity_usage_occurrences_per_week' + str(self.id)])
        self.save()
        return True


class WaterUsage(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)
    litres = models.IntegerField()
    occurrences_per_week = models.IntegerField()

    def __str__(self):
        return str(self.litres) + 'L, ' + str(self.occurrences_per_week) + ' times per week.'

    def save_water_usage(self, request):
        self.litres = int(request.POST['water_usage_litres' + str(self.id)])
        self.occurrences_per_week = int(request.POST['water_usage_occurrences_per_week' + str(self.id)])
        self.save()
        return True
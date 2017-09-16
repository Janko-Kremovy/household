from django.db import models


# The home style (eg. house/apartment)
class Dwelling(models.Model):
    type = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.type + ' @ ' + self.address


# The room type (eg. laundry/kitchen/living room)
class Room(models.Model):
    dwelling = models.ForeignKey(Dwelling, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


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


class ElectricityUsage(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)
    watts = models.IntegerField()
    time_minutes = models.IntegerField()
    occurrences_per_week = models.IntegerField()

    def __str__(self):
        return str(self.time_minutes) + ' minutes @ ' + str(self.watts) + 'W, ' + str(self.occurrences_per_week) + ' times per week.'


class WaterUsage(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)
    litres = models.IntegerField()
    occurrences_per_week = models.IntegerField()

    def __str__(self):
        return str(self.litres) + 'L, ' + str(self.occurrences_per_week) + ' times per week.'
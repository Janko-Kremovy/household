from django import forms
from django.forms import ModelForm

from expenses.models import Room, Appliance, ElectricityUsage


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name']


class ApplianceForm(ModelForm):
    class Meta:
        model = Appliance
        fields = ['type', 'make', 'model', 'year', 'uses_electricity', 'uses_water', 'uses_gas']


class ElectricityUsageForm(ModelForm):
    class Meta:
        model = ElectricityUsage
        fields = ['watts', 'time_minutes', 'occurrences_per_week']

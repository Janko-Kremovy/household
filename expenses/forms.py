from django import forms
from django.forms import ModelForm

from expenses.models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name']
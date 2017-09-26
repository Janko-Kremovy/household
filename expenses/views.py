from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import DeleteView

from expenses.models import Dwelling, Room, Appliance, ElectricityUsage, WaterUsage
from .forms import RoomForm, ApplianceForm, ElectricityUsageForm, WaterUsageForm


class RoomDelete(DeleteView):
    model = Room
    success_url = reverse_lazy('dwelling_detail', args=(1,))
    template_name = 'expenses/room_delete.html'


class ApplianceDelete(DeleteView):
        model = Appliance
        success_url = reverse_lazy('dwelling_detail', args=(1,))
        template_name = 'expenses/appliance_delete.html'


class ElectricityUsageDelete(DeleteView):
    model = ElectricityUsage
    success_url = reverse_lazy('dwelling_detail', args=(1,))
    template_name = 'expenses/electricity_usage_delete.html'


class WaterUsageDelete(DeleteView):
    model = WaterUsage
    success_url = reverse_lazy('dwelling_detail', args=(1,))
    template_name = 'expenses/water_usage_delete.html'


def room_add(request, dwelling_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RoomForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            new_room = Room()
            new_room.name = form.cleaned_data['name']
            new_room.dwelling = Dwelling.objects.get(pk=dwelling_id)
            new_room.save()
            return HttpResponseRedirect(reverse('dwelling_detail', args=(dwelling_id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RoomForm()

    return render(request, 'expenses/room_add.html', {'form': form, 'dwelling': Dwelling.objects.get(pk=dwelling_id)})


def appliance_add(request, room_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ApplianceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            new_appliance = Appliance()
            new_appliance.type = form.cleaned_data['type']
            new_appliance.make = form.cleaned_data['make']
            new_appliance.model = form.cleaned_data['model']
            new_appliance.year = form.cleaned_data['year']
            new_appliance.uses_electricity = form.cleaned_data['uses_electricity']
            new_appliance.uses_water = form.cleaned_data['uses_water']
            new_appliance.uses_gas = form.cleaned_data['uses_gas']
            new_appliance.room = Room.objects.get(pk=room_id)
            dwelling = Dwelling.objects.get(pk=Room.objects.get(pk=room_id).dwelling.id)
            new_appliance.save()
            return HttpResponseRedirect(reverse('dwelling_detail', args=(dwelling.id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ApplianceForm()

    return render(request, 'expenses/appliance_add.html', {'form': form, 'room': Room.objects.get(pk=room_id)})


def electricity_usage_add(request, appliance_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ElectricityUsageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            new_electricity_usage = ElectricityUsage()
            new_electricity_usage.watts = form.cleaned_data['watts']
            new_electricity_usage.time_minutes = form.cleaned_data['time_minutes']
            new_electricity_usage.occurrences_per_week = form.cleaned_data['occurrences_per_week']
            new_electricity_usage.appliance = Appliance.objects.get(pk=appliance_id)
            dwelling = Dwelling.objects.get(pk=new_electricity_usage.appliance.room.dwelling.id)
            new_electricity_usage.save()
            return HttpResponseRedirect(reverse('dwelling_detail', args=(dwelling.id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ElectricityUsageForm()

    return render(request, 'expenses/electricity_usage_add.html', {'form': form, 'appliance': Appliance.objects.get(pk=appliance_id)})


def water_usage_add(request, appliance_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WaterUsageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            new_water_usage = WaterUsage()
            new_water_usage.litres = form.cleaned_data['litres']
            new_water_usage.occurrences_per_week = form.cleaned_data['occurrences_per_week']
            new_water_usage.appliance = Appliance.objects.get(pk=appliance_id)
            dwelling = Dwelling.objects.get(pk=new_water_usage.appliance.room.dwelling.id)
            new_water_usage.save()
            return HttpResponseRedirect(reverse('dwelling_detail', args=(dwelling.id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WaterUsageForm()

    return render(request, 'expenses/water_usage_add.html', {'form': form, 'appliance': Appliance.objects.get(pk=appliance_id)})

def index(request):
    dwelling_list = Dwelling.objects.all
    context = {'dwelling_list': dwelling_list}
    return render(request, 'expenses/index.html', context)


def dwelling_detail(request, dwelling_id):
    dwelling = Dwelling.objects.get(pk=dwelling_id)
    context = {'dwelling': dwelling}
    return render(request, 'expenses/dwelling_detail.html', context)


def dwelling_update(request, dwelling_id):

    dwelling = Dwelling.objects.get(pk=dwelling_id)

    # Get POST data and update the entire dwelling.
    try:
        # DWELLING
        dwelling.save_dwelling(request)

        # EACH ROOM IN DWELLING
        for room in dwelling.room_set.all():
            room.save_room(request)

            # EACH APPLIANCE IN ROOM
            for appliance in room.appliance_set.all():
                appliance.save_appliance(request)

                # EACH ELECTRICITY USAGE FOR APPLIANCE
                if appliance.uses_electricity:
                    for electricity_usage in appliance.electricityusage_set.all():
                        electricity_usage.save_electricity_usage(request)

                # EACH WATER USAGE FOR APPLIANCE
                if appliance.uses_water:
                    for water_usage in appliance.waterusage_set.all():
                        water_usage.save_water_usage(request)

    # THIS SHOULD NOT HAPPEN
    except(KeyError, Dwelling.DoesNotExist):
        # Redisplay the update form.
        return render(request, 'expenses/dwelling_update.html', {
            'dwelling': dwelling,
            'error_message': "You didn't update an existing Dwelling",
        })

    return HttpResponseRedirect(reverse('dwelling_detail', args=(dwelling.id,)))
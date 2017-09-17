from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from expenses.models import Dwelling, Room
from .forms import RoomForm


def room_add(request):
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
            new_room.dwelling = form.cleaned_data['dwelling']
            new_room.save()
            return render(request, 'expenses/room_add.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RoomForm()

    return render(request, 'expenses/room_add.html', {'form': form})

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
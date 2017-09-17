from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from expenses.models import Dwelling


def index(request):
    dwelling_list = Dwelling.objects.all
    context = {'dwelling_list': dwelling_list}
    return render(request, 'expenses/index.html', context)


def detail(request, dwelling_id):
    dwelling = Dwelling.objects.get(pk=dwelling_id)
    context = {'dwelling': dwelling}
    return render(request, 'expenses/detail.html', context)


def update(request, dwelling_id):

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
        return render(request, 'expenses/update.html', {
            'dwelling': dwelling,
            'error_message': "You didn't update an existing Dwelling",
        })

    return HttpResponseRedirect(reverse('detail', args=(dwelling.id,)))
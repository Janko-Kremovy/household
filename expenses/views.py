from django.core.handlers.base import logger
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from expenses.models import Appliance, Dwelling, ElectricityUsage


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

    #Get POST data and update the entire dwelling.
    try:
        dwelling.type = request.POST['type'+str(dwelling.id)]
        dwelling.address = request.POST['address'+str(dwelling.id)]
        dwelling.save()

        for room in dwelling.room_set.all():
            room.name = request.POST['room_name'+str(room.id)]
            room.save()

            for appliance in room.appliance_set.all():
                appliance.type = request.POST['appliance_type'+str(appliance.id)]
                appliance.make = request.POST['appliance_make'+str(appliance.id)]
                appliance.model = request.POST['appliance_model'+str(appliance.id)]
                appliance.year = int(request.POST['appliance_year'+str(appliance.id)])
                appliance.save()

                if appliance.uses_electricity:
                    for electricity_usage in appliance.electricityusage_set.all():
                        electricity_usage.watts = int(request.POST['electricity_usage_watts' + str(electricity_usage.id)])
                        electricity_usage.time_minutes = int(request.POST['electricity_usage_time_minutes' + str(electricity_usage.id)])
                        electricity_usage.occurrences_per_week = int(request.POST['electricity_usage_occurrences_per_week' + str(electricity_usage.id)])
                        electricity_usage.save()

    except(KeyError, Dwelling.DoesNotExist):
        # Redisplay the update form.
        return render(request, 'expenses/update.html', {
            'dwelling': dwelling,
            'error_message': "You didn't update an existing Dwelling",
        })

    return HttpResponseRedirect(reverse('detail', args=(dwelling.id,)))
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from racerapp.models import Race, Participant


# Create your views here.
def list_races(request):
    races = Race.objects.values()
    return render(request, 'list.html', {"races": races})


def register(request, racename=''):
    return render(request, 'register.html', {"racename": racename})


def submit(request):
    name = request.POST.get('name', '')
    address = request.POST.get('address', '')
    racename = request.POST.get('racename', '')
    age = request.POST.get('age', '')
    r = Race(name=racename)
    p = Participant()
    status = ''
    if name and address and racename and age:
        try:
            r = Race.objects.get(name=racename)
            p = Participant(name=name, address=address, age=age, race=r)
            p.save()
            status='registered'
        except ValueError:
            status = 'failed'

    print('status: ', status)
    return render(request, 'register.html', {"racename": racename, "status": status})


def participants(request, racename=''):
    race = Race.objects.get(name=racename)
    participants = Participant.objects.filter(race=race)
    print(participants)

    data = serializers.serialize('json', participants )

    response = HttpResponse(data)
    response['content_type'] = 'application/json'

    return response

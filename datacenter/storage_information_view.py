from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
import datetime


def get_duration(visit):
    delta = timezone.localtime(timezone.now()) - timezone.localtime(visit.entered_at)
    return delta.total_seconds()


def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    return f'{hours:02}:{minutes:02}'


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at__isnull=True):
        visit_dict = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': format_duration(get_duration(visit))
        }
        non_closed_visits.append(visit_dict)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

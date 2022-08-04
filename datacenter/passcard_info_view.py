from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.utils import timezone
import datetime

def get_duration(visit):
    if visit.leaved_at is None:
        delta = timezone.localtime(timezone.now()) - timezone.localtime(visit.entered_at)
    else:
        delta = timezone.localtime(visit.leaved_at) - timezone.localtime(visit.entered_at)
    return delta.total_seconds()

def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    return f'{hours:02}:{minutes:02}'

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = get_list_or_404(Visit, passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        duration = get_duration(visit)
        visit_dict = {
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': format_duration(duration),
            'is_strange': duration > 3600
        }
        this_passcard_visits.append(visit_dict)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

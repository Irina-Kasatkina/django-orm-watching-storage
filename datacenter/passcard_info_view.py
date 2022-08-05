from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.utils import timezone

from . import visit_duration

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = get_list_or_404(Visit, passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        duration = visit_duration.get_duration(visit)
        visit_dict = {
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': visit_duration.format_duration(duration),
            'is_strange': duration > visit_duration.SECONDS_IN_HOUR
        }
        this_passcard_visits.append(visit_dict)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

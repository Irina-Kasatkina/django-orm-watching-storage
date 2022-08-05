from datacenter.models import Visit
from django.utils import timezone
import datetime

MINUTES_IN_HOUR = 60
SECONDS_IN_HOUR = 3600

def get_duration(visit):
    if visit.leaved_at is None:
        delta = timezone.localtime(timezone.now()) - timezone.localtime(visit.entered_at)
    else:
        delta = timezone.localtime(visit.leaved_at) - timezone.localtime(visit.entered_at)
    return delta.total_seconds()

def format_duration(duration):
    hours = int(duration // SECONDS_IN_HOUR)
    minutes = int((duration % SECONDS_IN_HOUR) // MINUTES_IN_HOUR)
    return f'{hours:02}:{minutes:02}'
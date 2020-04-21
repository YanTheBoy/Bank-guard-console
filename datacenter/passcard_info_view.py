from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import get_passcard


def passcard_info_view(request, passcode):
  this_passcard_visits = []
  card = Passcard.objects.get(passcode=passcode)
  entered = Visit.objects.filter(passcard=card)
  for attendance in entered:
    passcard = get_passcard(attendance)
    this_passcard_visits.append(
      {
        'entered_at': passcard['entered_at'],
        'duration': passcard['duration'],
        'is_strange': passcard['is_strange']
      }
    )

  context = {
      "passcard": card,
      "this_passcard_visits": this_passcard_visits
  }
  return render(request, 'passcard_info.html', context)

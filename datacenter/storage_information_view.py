from datacenter.models import Visit
from django.shortcuts import render
from .models import get_storage_visitor


def storage_information_view(request):
  non_closed_visits = [ ]
  visitors_inside = Visit.objects.filter(leaved_at__isnull=True)
  for visitor in visitors_inside:
    visitor = get_storage_visitor(visitor)
    non_closed_visits.append(
      {
        'who_entered': visitor['who_entered'],
        'entered_at': visitor['entered_at'],
        'duration': visitor['duration'],
        'is_strange': visitor['is_strange']
      }
    )
 
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

from django.db import models
import django.utils.timezone as tz

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )


def get_duration(time_from, time_entered):
  if time_from is None:
    time_now = tz.localtime(tz.now())
    duration = (time_now-time_entered).total_seconds()
  else:
    duration = (time_from-time_entered).total_seconds()
  return duration


def format_duration(duration):
    formatted_hours = int(duration//3600)
    formatted_min =  int((duration%3600)//60)
    duration = '{}ч {}мин'.format(formatted_hours, formatted_min)
    return duration


def is_visit_long(duration):
  return int(duration) > 3600


def get_storage_visitor(visitor):
  visitor_entered = tz.localtime(visitor.entered_at)
  local_time_now = tz.localtime(tz.now())
  
  duration = get_duration(local_time_now, visitor_entered)
  strange_visit = is_visit_long(duration)
  formatted_duration = format_duration(duration)
  return {
        'who_entered': visitor.passcard,
        'entered_at': visitor_entered,
        'duration': formatted_duration,
        'is_strange': strange_visit
      }


def get_passcard(visit):
  entered = tz.localtime(visit.entered_at)
  leaved = tz.localtime(visit.leaved_at)

  visit_duration = get_duration(leaved, entered)
  formatted_duration = format_duration(visit_duration)
  long_visit = is_visit_long(visit_duration)

  return {
          'entered_at': visit.entered_at.date(),
      'duration': formatted_duration,
      'is_strange': long_visit
  }

  
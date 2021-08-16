from django import template
from django.template.defaultfilters import stringfilter
from workflow.models import Status, Document, Submission


register = template.Library()


#@register.filter
#def duration(td):
#    ''' formats seconds to weeks and days '''
#    total_seconds = int(td.total_seconds())
#    weeks = total_seconds // 604800
#    days = (total_seconds % 604800) //86400  
#    return '{} w {} d'.format(weeks, days)
#register.filter('duration', duration)

@register.filter
def hoursToInt(td):
    ''' converts hourt to int '''
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    res =  int(hours)
    return res
register.filter('hoursToInt', hoursToInt)

@property
def is_past_due(self):
    return date.today() > self.date



#STATUS
#GA Status
@register.simple_tag
def ga_qty(qs, phase_no):
    count = 0   
    for doc in qs:
        if doc.type == 4 and doc.phase.pk == phase_no and doc.withdrawn == False:
            count+=1
    return count            
register.filter('ga_qty', ga_qty)

@register.simple_tag
def ga_status_a(qs, phase_no):
    count = 0
    for status in qs:
        if status.submission.document.phase.pk == phase_no and status.status == 0 and status.submission.document.type == 4 and status.active == True and status.submission.document.withdrawn == False:
            count+=1
    return count
register.filter('ga_status_a', ga_status_a)

@register.simple_tag
def ga_status_b(qs, phase_no):
    count = 0
    for status in qs:
        if status.submission.document.phase.pk == phase_no and status.status == 1 and status.submission.document.type == 4 and status.active == True and status.submission.document.withdrawn == False:
            count+=1
    return count
register.filter('ga_status_b', ga_status_b)

@register.simple_tag
def ga_status_c(qs, phase_no):
    count = 0
    for status in qs:
        if status.submission.document.phase.pk == phase_no and status.status == 2 and status.submission.document.type == 4 and status.active == True and status.submission.document.withdrawn == False:
            count+=1
    return count            
register.filter('ga_status_c', ga_status_c)

@register.simple_tag
def ga_issued(qs, phase_no):
    count = 0
    for submission in qs:
        if submission.document.phase.pk == phase_no and submission.document.type == 4 and submission.active == True and submission.document.withdrawn == False:
            count+=1
    return count            
register.filter('ga_issued', ga_issued)

@register.simple_tag
def ga_not_issued(qs, phase_no):
    count = 0   
    for doc in qs:
        if doc.submissions.all().count() == 0  and doc.type == 4 and doc.phase.pk == phase_no and doc.withdrawn == False:
            count+=1
    return count            
register.filter('ga_not_issued', ga_not_issued)

#TS Status
@register.simple_tag
def ts_qty(qs, phase_no):
    count = 0   
    for doc in qs:
        if doc.type == 3 and doc.phase.pk == phase_no and doc.withdrawn == False:
            count+=1
    return count            
register.filter('ts_qty', ts_qty)

@register.simple_tag
def ts_status_a(qs, phase_no):
    count = 0
    for status in qs:
        if status.submission.document.phase.pk == phase_no and status.status == 0 and status.submission.document.type == 3 and status.active == True and status.submission.document.withdrawn == False:
            count+=1
    return count
register.filter('ts_status_a', ts_status_a)

@register.simple_tag
def ts_status_b(qs, phase_no):
    count = 0
    for status in qs:
        if status.submission.document.phase.pk == phase_no and status.status == 1 and status.submission.document.type == 3 and status.active == True and status.submission.document.withdrawn == False:
            count+=1
    return count
register.filter('ts_status_b', ts_status_b)

@register.simple_tag
def ts_status_c(qs, phase_no):
    count = 0
    for status in qs:
        if status.submission.document.phase.pk == phase_no and status.status == 2 and status.submission.document.type == 3 and status.active == True and status.submission.document.withdrawn == False:
            count+=1
    return count            
register.filter('ts_status_c', ts_status_c)

@register.simple_tag
def ts_issued(qs, phase_no):
    count = 0
    for submission in qs:
        if submission.document.phase.pk == phase_no and submission.document.type == 3 and submission.active == True and submission.document.withdrawn == False:
            count+=1
    return count            
register.filter('ts_issued', ts_issued)

@register.simple_tag
def ts_not_issued(qs, phase_no):
    count = 0   
    for doc in qs:
        if doc.submissions.all().count() == 0  and doc.type == 3 and doc.phase.pk == phase_no and doc.withdrawn == False:
            count+=1
    return count            
register.filter('ts_not_issued', ts_not_issued)







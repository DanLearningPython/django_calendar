from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from .forms import EventForm
from .models import Event
from .utils import get_type_border_color, get_user_color, format_event_title


def index(request):

    return render(request, 'oncall/calendar.html', {'data': '','page_name' :'calendar'})


def test(request):

    return render(request, 'oncall/test.html', {'data': '', 'page_name' : 'test'})


def event_create(request):

    data = dict()

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        data = {'user' : request.user.id}
        form = EventForm(initial=data)

    context = {'form': form}
    data['html_form'] = render_to_string('oncall/forms/event_create.html',
        context,
        request=request,
    )
    return JsonResponse(data)


def event_update(request, id):

    data = dict()

    event = get_object_or_404(Event, pk=id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = EventForm(instance=event)

    context = {'form': form, 'id': id}
    data['html_form'] = render_to_string('oncall/forms/event_update.html',
        context,
        request=request
    )
    return JsonResponse(data)


def event_feed(request):

    events = Event.objects.all()
    output_events = []
    result = {}

    datetime_format = '%Y-%m-%d %H:%M:%S'

    for event in events:
        tmp = {}
        tmp['id'] = event.id
        tmp['title'] = format_event_title(event.user_id, event.event_name, event.event_type)
        #tmp['event_type'] = event.event_type.event_type_name
        #event_start_timestamp = time.mktime(event.event_start.timetuple())
        #event_end_timestamp = time.mktime(event.event_end.timetuple())
        tmp['start'] = event.event_start
        tmp['end'] = event.event_end
        tmp['data_url'] = '/update' + '/' + str(event.id)
        tmp['className'] = 'js-update-event'
        tmp['borderColor'] = 'white'
        if(event.event_type.event_type_name == 'On call'):
            tmp['backgroundColor'] = get_user_color(event.user_id)
            tmp['textColor'] = 'black'
        else:
            tmp['textColor'] ='black'
            tmp['backgroundColor'] = 'white'
            tmp['borderColor'] = get_user_color(event.user_id)

        output_events.insert(0,tmp)

    result['events'] = output_events

    return JsonResponse(result['events'], safe=False)

from .models import EventType, Profile, User


def get_user_color(uid):
    try:
        user_color = Profile.objects.get(user_id=uid)
        return user_color.color
    except Profile.DoesNotExist:
        return 'red'


def get_type_border_color(type):

    try:
        type = EventType.objects.get(event_type_name=type)
        return type.event_type_color
    except EventType.DoesNotExist:
        return 'none'


def format_event_title(uid, event_title, event_type):
    title = ''

    try:
        user = User.objects.get(id=uid)
        title += user.first_name + ' ' + user.last_name[0] + ' - '
    except Profile.DoesNotExist:
        pass

    title += event_title

    try:
        event_type_abbrev = EventType.objects.get(event_type_name=event_type)
        title += ' ( ' + event_type_abbrev.event_type_abbrev + '.) '
    except EventType.DoesNotExist:
        pass

    return title
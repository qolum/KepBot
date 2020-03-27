from bot.models import Schedule


def find_group(message):
    for group in Schedule.object.filter(group__group_name__exact=message.lower()):
        name = group.group
    return str(name)


def get_schedule(callback):
    response = []
    day, group = callback.split(',')
    result = Schedule.object.filter(group__group_name__startswith=group.lower()).filter(weekday=day)
    for element in result:
        response.append(
            f'<b>{str(element.time)[0]}) {str(element.subject)}, {str(element.classroom)},{str(element.teachers)}</b>')
    return sorted(response)

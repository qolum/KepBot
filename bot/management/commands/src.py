from datetime import datetime

from bot.models import Schedule, Teachers, Groups
from .message import DONT_FIND_MESSAGE


def get_schedule_for_student(request):
    response = []
    obj = Schedule.object.filter(group__group_name__iexact=eval(request)[2]).filter(weekday=eval(request)[1])
    for element in obj:
        response.append(
            f'<b>{str(element.time)[0]}) {str(element.subject)}, {str(element.classroom)},{str(element.teachers)}</b>')
    return sorted(response)


def get_schedule_for_teacher(request):
    response = []
    obj = Schedule.object.filter(teachers__teachers_name__iexact=eval(request)[2]).filter(weekday=eval(request)[1])
    for element in obj:
        response.append(
            f"<b>{str(element.time)[0]}) {str(element.group)}, {str(element.classroom)}</b>")
    return sorted(response)


def get_teachers(name):
    response = []
    for teacher in Teachers.object.filter(teachers_name__startswith=name).values_list('teachers_name'):
        if teacher not in response:
            response.append(teacher[0])
    if not response:
        response = 'Empty'
    return response


def get_groups(name):
    response = []
    for group in Groups.object.filter(group_name__startswith=name).values_list('group_name'):
        if group not in response:
            response.append(group[0])
    if not response:
        response = 'Empty'
    return response


def get_lecture_for_teacher(name):
    response = []
    now = datetime.now().hour
    for obj in Schedule.object.filter(time__beginning__hour__gte=now).filter(
            teachers__teachers_name__iexact=name[1]).order_by('time'):
        response.append(
            f"<b>Група: {str(obj.group)}\nАудиторія: {str(obj.classroom)}</b>")
    if not response:
        return DONT_FIND_MESSAGE
    else:
        return response


def get_lecture_for_student(data):
    response = []
    now = datetime.now().hour
    for obj in Schedule.object.filter(time__beginning__hour__gte=now).filter(
            group__group_name__iexact=data[1]).order_by('time'):
        response.append(
            f"<b>Вчитель: {str(obj.teachers)}\nПредмет: {str(obj.subject)}\nАудиторія: {str(obj.classroom)}</b>")
    if not response:
        return DONT_FIND_MESSAGE
    else:
        return response

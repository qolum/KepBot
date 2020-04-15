from django.contrib import admin
from .models import Classroom, Teachers, Schedule, Groups, Subject


# Register your models here.
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teachers', 'group', 'classroom', 'weekday', 'time')
    search_fields = ('subject', 'teachers', 'group', 'classroom', 'weekday', 'time')


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('classroom',)
    search_fields = ('classroom',)


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('group_name',)
    search_fields = ('group_name',)


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('teachers_name',)
    search_fields = ('teachers_name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject',)
    search_fields = ('subject',)

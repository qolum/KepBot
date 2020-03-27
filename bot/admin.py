from django.contrib import admin
from .models import Classroom, Teachers, Schedule, Groups, Subject

# Register your models here.
admin.site.register(Schedule)
admin.site.register(Classroom)
admin.site.register(Groups)
admin.site.register(Teachers)
admin.site.register(Subject)

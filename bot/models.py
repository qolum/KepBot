from django.db import models


class Teachers(models.Model):
    teachers_name = models.CharField(max_length=20, unique=True, db_index=True, verbose_name='Вчитель')
    object = models.Manager()

    class Meta:
        verbose_name = 'Вчитель'
        verbose_name_plural = 'Вчителя'

    def __str__(self):
        return self.teachers_name


class Groups(models.Model):
    group_name = models.CharField(max_length=30, unique=True, db_index=True, verbose_name='Група')
    object = models.Manager()

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Групи'

    def __str__(self):
        return self.group_name


class Time(models.Model):
    number = models.IntegerField()
    beginning = models.TimeField()
    ending = models.TimeField()

    def __str__(self):
        return f"{self.number},{self.beginning},{self.ending}"


class Classroom(models.Model):
    classroom = models.CharField(max_length=30, unique=True, db_index=True, verbose_name='Аудиторія')

    class Meta:
        verbose_name = 'Аудиторія'
        verbose_name_plural = 'Аудиторії'

    def __str__(self):
        return self.classroom


class Subject(models.Model):
    subject = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмети'

    def __str__(self):
        return self.subject


class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, verbose_name='Предмет')
    teachers = models.ForeignKey(Teachers, on_delete=models.DO_NOTHING, verbose_name='Вчитель')
    group = models.ForeignKey(Groups, on_delete=models.DO_NOTHING, verbose_name='Група')
    time = models.ForeignKey(Time, on_delete=models.DO_NOTHING, verbose_name='Пара')
    classroom = models.ForeignKey(Classroom, on_delete=models.DO_NOTHING, verbose_name='Аудиторія')
    weekday = models.CharField(max_length=200,
                               choices=(
                                   ('1', 'Понеділок'),
                                   ('2', 'Вівторок'),
                                   ('3', 'Середа'),
                                   ('4', 'Четверг'),
                                   ('5', "П'ятниця")),
                               verbose_name='День тижня')
    object = models.Manager()

    class Meta:
        verbose_name = 'Заняття'
        verbose_name_plural = 'Розклад'
        ordering = ["time"]

    def __str__(self):
        return f"{self.group, self.teachers, self.subject, self.time, self.classroom, self.weekday}"

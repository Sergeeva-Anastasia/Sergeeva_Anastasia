from django.db import models

class Chanells(models.Model):
  title = models.CharField(max_length=50, verbose_name='Название')
  content = models.TextField(null=True, blank=True, verbose_name='Описание')

  class Meta:
    verbose_name_plural = 'Телеканалы'
    verbose_name = 'Телеканал'


class TVShows(models.Model):
  title = models.CharField(max_length=30, verbose_name='Название передачи')
  content = models.TextField(null=True, blank=True, verbose_name='Описание')
  type = models.TextField(null=True, blank=True, verbose_name='Тип передачи')
  chanell = models.TextField(null=True, blank=True, verbose_name='Канал трансляции')
  timestart = models.TimeField(null=True, blank=True, verbose_name='Время начала')
  timeend = models.TimeField(null=True, blank=True, verbose_name='Время окончания')

  class Meta:
    verbose_name_plural = 'Передачи'
    verbose_name = 'Передача'


class Type(models.Model):
  title = models.CharField(max_length=30, verbose_name='Название типа передачи')
  content = models.IntegerField(null=True, blank=True, verbose_name='Возрастной ценз')

  class Meta:
    verbose_name_plural = 'Типы передач'
    verbose_name = 'Тип передач'


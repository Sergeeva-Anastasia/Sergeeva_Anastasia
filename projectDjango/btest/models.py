from django.db import models

class Chanells(models.Model):
  title = models.CharField(max_length=50)
  content = models.TextField(null=True, blank=True)
  price = models.FloatField(null=True, blank=True)
  published = models.DateTimeField(auto_now_add=True, db_index=True)

from btest.models import Chanells
b1 = Chanells(title='Россия 1', content='Телеканал «Россия 1» — это информационно-развлекательный телеканал, флагман ВГТРК.')


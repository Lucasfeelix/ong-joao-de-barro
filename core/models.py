from django.db import models


class TimeModel(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        abstract = True

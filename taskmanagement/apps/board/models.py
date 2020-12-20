from django.db import models

from apps.core.models import TimeStampModel

# Create your models here.
class Board(TimeStampModel):
    name = models.CharField(max_length=255, unique=True)
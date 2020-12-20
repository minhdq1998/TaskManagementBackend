from django.db import models

class TimeStampModel(models.Model):

    """
    Abstract Model: Use for model which have created and modified fields
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

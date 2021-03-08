from django.db import models
from base.utils import get_unique_id


class TimestampedIdModel(models.Model):
    id = models.CharField(max_length=16, default=get_unique_id, primary_key=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)

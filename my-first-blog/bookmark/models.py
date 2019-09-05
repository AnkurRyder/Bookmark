from django.db import models
from django.contrib.auth.models import User

DEFAULT_USER_ID =1
class Data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=DEFAULT_USER_ID)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date')
    freq = models.IntegerField(default=0)

    def __str__(self):
        return self.title
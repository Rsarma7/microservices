from django.db import models
import datetime
# Create your models here.
class todo(models.Model):
    todo_des = models.CharField(max_length=1000,null=False)
    username = models.CharField(max_length=100,null=False)
    created_date = models.DateField(default=datetime.date.today)




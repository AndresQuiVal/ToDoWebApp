from django.db import models
import datetime

# Create your models here.

class Priority(models.Model):
    prior_type = models.CharField(verbose_name="type", max_length=30)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.prior_type

class ToDo(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.datetime.now())
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)

    def __str__(self):
        return " %s, %s, %s" %(self.name, self.description, self.priority.prior_type)


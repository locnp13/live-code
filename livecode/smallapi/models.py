from django.db import models

# Create your models here.


class TwoNumberSum(models.Model):
    id = models.AutoField(primary_key=True)
    first_num = models.IntegerField(null=False)
    second_num = models.IntegerField(null=False)
    sum = models.IntegerField(null=True)

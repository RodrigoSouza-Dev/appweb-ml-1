from django.db import models
class Patient(models.Model):
    name = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100, null=False)
    age = models.FloatField(null=False)
    gender = models.FloatField(null=False)
    weight = models.FloatField(null=False)
    height = models.FloatField(null=False)
    diastolic_pressure = models.FloatField(null=False)
    systolic_pressure = models.FloatField(null=False)
    cholesterol = models.FloatField(null=False, default=0)
    glucose = models.FloatField(null=False, default=0)
    smoker = models.IntegerField(null=False, default=0)
    alcohol_intake = models.IntegerField(null=False, default=0)  # Set the default value as per your requirement
    physical_activity = models.IntegerField(null=False, default=0)
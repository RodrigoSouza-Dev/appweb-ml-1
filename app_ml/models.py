"""from django.db import models

class Cardio(models.Model):
    id = models.AutoField(primary_key=True)
    gender = models.IntegerField(choices=((1, 'Female'), (2, 'Male')))
    height = models.FloatField()
    weight = models.FloatField()
    systolic_pressure = models.IntegerField()
    diastolic_pressure = models.IntegerField()
    cholesterol = models.IntegerField(choices=((1, 'Normal'), (2, 'Above normal'), (3, 'Well above normal')))
    glucose = models.IntegerField(choices=((1, 'Normal'), (2, 'Above normal'), (3, 'Well above normal')))
    smoker = models.IntegerField()
    alcohol_intake = models.IntegerField()
    physical_activity = models.IntegerField()"""


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
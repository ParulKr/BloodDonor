from django.db import models

class BloodDRList(models.Model):
    #SNo=models.AutoField
    BDName=models.CharField(max_length=100)
    Sex=models.CharField(max_length=100)
    Age=models.IntegerField()
    location=models.CharField(max_length=100)
    BloodGP=models.CharField(max_length=100)
    def __str__(self):
        return self.BDName


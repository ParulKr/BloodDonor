from django.db import models
class sqlservercon(models.Model):
    MovieName=models.CharField(max_length=100)
    Budget=models.IntegerField()
    IMDBrating=models.IntegerField()
    link= models.CharField(max_length=400)
    image= models.ImageField(upload_to="IMDBMoviesList/images", default='')


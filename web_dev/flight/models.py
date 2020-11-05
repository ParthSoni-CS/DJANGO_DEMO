from django.db import models

# Create your models here.
class airport(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=30)

    def __str__(self):
        return f"Airport - {self.city}({self.code})"

class flight(models.Model):
    origin = models.ForeignKey(airport,on_delete=models.CASCADE,related_name="departure")
    destination = models.ForeignKey(airport,on_delete=models.CASCADE,related_name="arrival")
    duration = models.IntegerField()

    def __str__(self):
        return f" {self.origin} to {self.destination} in {self.duration} mins"

class passengers(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    flights = models.ManyToManyField(flight,blank=True,related_name="passengers")

    def __str__(self):
        return f"passenger({self.first_name} {self.last_name})"



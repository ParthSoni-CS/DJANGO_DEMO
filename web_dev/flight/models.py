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

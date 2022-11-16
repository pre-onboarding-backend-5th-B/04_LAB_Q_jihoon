from django.db import models

class SeoulGu(models.Model):
    name = models.CharField(max_length=10)
    drain_gu_code = models.CharField(max_length=3)
    rain_gu_code = models.CharField(max_length=3, blank=True)
    
    def __str__(self):
        return self.name

class DrainLocation(models.Model):
    location_info = models.CharField(max_length=200)
    location_code = models.CharField(max_length=7)
    gu = models.ForeignKey(SeoulGu, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.location_code} / {self.location_info}"

class RainLocation(models.Model):
    location_info = models.CharField(max_length=200)
    location_code = models.CharField(max_length=4)
    gu = models.ForeignKey(SeoulGu, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.location_code} / {self.location_info}"
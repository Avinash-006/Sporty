from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.event_name

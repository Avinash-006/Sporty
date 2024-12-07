from django.db import models

class Match(models.Model):
    match_name = models.CharField(max_length=100)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.date}"

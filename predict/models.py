from django.db import models
from ML.Main import main

class Character(models.Model):
    image = models.ImageField()
    actual_character = models.CharField(max_length=10)
    predicted_character = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.actual_character

    def save(self, *args, **kwargs):
        
        return super().save(*args, *kwargs)
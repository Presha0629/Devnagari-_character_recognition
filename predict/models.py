from django.db import models

class Character(models.Model):
    image = models.ImageField(null=False, blank=False)
    predicted_character = models.CharField(max_length=10)
    actual_character = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.actual_character

    
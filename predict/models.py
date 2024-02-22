from django.db import models
import cv2
import os
from django.conf import settings
from ML.Main import main

class Character(models.Model):
    image = models.ImageField(upload_to="images", blank=False, null=False)
    actual_character = models.CharField(max_length=10)
    predicted_character = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.actual_character

    def save(self, *args, **kwargs):
        return super().save(*args, *kwargs)
    
    def predict_character(self):
        # Path = os.path.join(settings.MEDIA_ROOT, self.image.name)
        # print("DEBUG::Read value type = ", type(cv2.imread(Path)))
        return (main(self.image.name))
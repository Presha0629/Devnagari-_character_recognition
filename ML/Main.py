import os
import cv2


from ML import Split_Words
from ML import Split_Characters
from ML import Predict_Characters

from django.conf import settings

def main(image_name):
    Path = os.path.join(settings.MEDIA_ROOT, image_name)
    # print("DEBUG::Read value type = ", type(cv2.imread(Path)))

    Words = Split_Words.Split(cv2.imread(Path))
    Characters = Split_Characters.Split(Words)
    Predictions = Predict_Characters.Predict(Characters)

    Words = []
    for Prediction in Predictions:
        Word = ''.join(Prediction)
        Words.append(Word)
    Words = ' '.join(Words)

    return(Words)
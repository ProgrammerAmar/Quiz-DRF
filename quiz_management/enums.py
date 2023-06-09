from django.db import models


class QuestionTypes(models.TextChoices):
    SINGLE_CORRECT = 'single', 'Single Correct' 
    MULTI_CORRECT = 'multi', 'Multi Correct' 
    
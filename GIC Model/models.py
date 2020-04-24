from django.db import models

# Create your models here.
class PredictModel(models.Model):
    MODEL_CHOICE = (
            ('GIC Purchase', 'GIC Purchase'),
            ('GIC Renewal', 'GIC Renewal'))
    target = models.CharField(max_length = 15, choices = MODEL_CHOICE)
    file = models.FileField()


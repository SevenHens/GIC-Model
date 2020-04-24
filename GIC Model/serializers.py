# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:40:48 2020

@author: e-sshen
"""

from rest_framework import serializers
from . models import PredictModel

class PredictSerializers(serializers.ModelSerializer):
    class Meta:
        model = PredictModel
        fields = '__all__'

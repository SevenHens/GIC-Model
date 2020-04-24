# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:27:53 2020

@author: e-sshen
"""
from django import forms

class PredictForm(forms.Form):
    Target = forms.ChoiceField(choices=[('GIC Purchase', 'GIC Purchase'), ('GIC Renewal', 'GIC Renewal')])
    File = forms.FileField()
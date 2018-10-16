from django import forms
from .models import FormModel, NonProfitModel


class Forms(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = {'timeCook', 'recipe', 'name'}
        order_field = ['name', 'recipe', 'timeCook']


class OtherForms(forms.ModelForm):
    class Meta:
        otherModel = NonProfitModel
        otherFields = {'name', 'address', 'establishedDate', 'operatingBudget', 'NumOfEmployees'}

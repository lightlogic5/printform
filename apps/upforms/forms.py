from django import forms
from django.utils import timezone

from .models import PrintForm




class MyPrintForm(forms.ModelForm):
    class Meta:
        model = PrintForm
        fields = ['repair_man', 'unit', 'content', 'telephone', 'pub_date']
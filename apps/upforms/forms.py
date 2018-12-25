from django import forms
from django.utils import timezone

from .models import PrintForm


class MyPrintForm(forms.ModelForm):
    class Meta:
        model = PrintForm
        # exclude = ['service_category', 'receive_date', 'over_date', 'back_date']
        fields = ['pub_date', 'repair_man', 'content','prints']
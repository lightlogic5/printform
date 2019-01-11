from django import forms
from django.forms import ModelForm,  TextInput, FileInput, Select
from .models import Prints

class PrintForm(ModelForm):
    class Meta:
        model = Prints
        exclude = ('user', 'service_num', 'comment','state')

        widgets = {
        }

        labels = {
            'name': '产品名称',
            'code': '产品代码',
        }

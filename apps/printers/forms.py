from django import forms
from django.forms import ModelForm,  TextInput, FileInput, Select
from django.forms import fields as Ffields
from django.forms import widgets as wid
from .models import Prints

class PrintForm(ModelForm):
    pub_date = Ffields.CharField(
        widget=wid.DateInput(attrs={"id":"my-datepicker"}),
        label='接收日期',
    )
    # pub_date = pub_date1 + '00:00'
    class Meta:
        model = Prints
        exclude = ('user', 'service_num', 'comment','state')

        widgets = {
            # "pub_date":wid.DateTimeInput(attrs={"class":"c1"}),
        }

        labels = {
            'pub_date': '发放的日期',
            'code': '产品代码',
        }

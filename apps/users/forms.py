from django import forms
from django.utils import timezone

from .models import Employee

# 用户登录
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

# 用户信息展示
class UserForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

# 用户姓名修改
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ['name','moblie','email','birthday', 'gender']
        # fields = ['name', 'moblie', 'email']

# class UploadImageForm(forms.Form):
#     name = forms.CharField(label='First Name', max_length=50, required=False)




# 用户个人信息修改表单
class SignupForm(forms.Form):

    def signup(self, request, user):
        user_profile = Employee()
        user_profile.user = user
        user.save()
        user_profile.save()
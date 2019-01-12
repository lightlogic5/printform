from django import forms
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Employee

# 用户注册
class RegistrationForm(forms.Form):

    username = forms.CharField(label='员工编号', max_length=50)
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    # Use clean methods to define custom validation rules

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) > 50:
            raise forms.ValidationError("用户名过长")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError("Your username already exists.")

        return username


    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 6:
            raise forms.ValidationError("Your password is too short.")
        elif len(password1) > 20:
            raise forms.ValidationError("Your password is too long.")

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password mismatch. Please enter again.")

        return password2

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
        fields = ['name','moblie','email','birthday', 'gender','units']
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
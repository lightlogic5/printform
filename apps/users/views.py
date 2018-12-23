from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .forms import LoginForm
# Create your views here.
from .models import Employee
from .forms import UserForm, UploadImageForm



class LogoutView(View):
    """
    用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))

class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "login.html", {"msg":"用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form":login_form})


# 用户信息展示
@login_required
def profile(request):
    user = request.user
    return render(request, 'employee.html', {'user': user})

@login_required
def profile_update(request):
    user = request.user
    user_profile = get_object_or_404(Employee, user=user)

    if request.method == "POST":
        form = UploadImageForm(request.POST)

        if form.is_valid():
            user_profile.save()

            return HttpResponseRedirect(reverse('myaccount:profile'))
    else:
        default_data = {'name': user_profile.name, }
        form = UploadImageForm(default_data)

    return render(request, 'employee.html', {'form': form, 'user': user})

# 用户信息维护


class UserView(View):

    def get(self, request):
        user = request.user
        return render(request, 'employee.html', {'user': user})

    def post(self, request):
        user = request.user
        user_profile = get_object_or_404(Employee, user=user)
        user_form = UploadImageForm(request.POST)
        if user_form.is_valid():
            user_profile.name = user_form.cleaned_data['name']
            user_profile.birthday = user_form.cleaned_data['birthday']
            user_profile.moblie = user_form.cleaned_data['moblie']
            user_profile.email = user_form.cleaned_data['email']
            user_profile.gender = user_form.cleaned_data['gender']
            user_profile.save()
            return HttpResponseRedirect(reverse('users:employee'))
        else:
            return HttpResponse('{"status":"fail", "msg":"个人资料修改失败"}', content_type='application/json')

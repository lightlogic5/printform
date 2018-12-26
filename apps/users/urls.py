from django.urls import path, re_path

from . import views

urlpatterns = [
    # 员工信息页
    path('employee/',views.UserView.as_view(), name='employee'),
    # 登出页
    path('logout/', views.LogoutView.as_view(), name="logout"),
    # 提交表单
]
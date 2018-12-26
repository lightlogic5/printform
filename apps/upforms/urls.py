from django.urls import path

from . import views

urlpatterns = [
    # 故障提交
    path('', views.UpFormView.as_view(), name='upform'),
    # 故障列表
    path('list/', views.FormListView.as_view(), name='formlist'),
    # path('list/', FormListView.as_view(), name='formlist'),
]




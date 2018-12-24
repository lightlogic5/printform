from django.urls import path

from . import views

urlpatterns = [
    path('', views.UpFormView.as_view(), name='upform'),
    # path('list/', FormListView.as_view(), name='formlist'),
]




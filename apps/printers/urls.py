from django.urls import path

from .views import updatepr,PrintCreate, delpr

urlpatterns = [
    # 打印机更新
    path('updatepr/<int:pk>/',  updatepr.as_view(), name='update'),
    path('prdelete/<int:pk>/', delpr.as_view(), name='delete'),
    path('create/',  PrintCreate.as_view(), name='create'),
]

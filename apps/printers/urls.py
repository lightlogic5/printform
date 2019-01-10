from django.urls import path

from .views import updatepr

urlpatterns = [
    # 打印机更新
    path('updatepr/<int:pk>/',  updatepr.as_view(), name='update'),
    # path('prdelete/<int:id>/', tododelete, name='delete'),
]

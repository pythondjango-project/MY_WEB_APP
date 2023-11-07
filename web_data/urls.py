from django.urls import path
from . import views 

urlpatterns=[
    path('list',views.MyWebData.as_view(),name='webdata_read'),
    path('list/<int:pk>/',views.MyWebData.as_view(),name='webdata_detail'),

]
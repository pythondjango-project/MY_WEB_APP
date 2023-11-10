from django.urls import path
from . import views 

urlpatterns=[
    path('webdata',views.MyWebData.as_view(),name='webdata'),
   # path('list/<int:pk>/',views.MyWebData.as_view(),name='webdata_detail'),

]
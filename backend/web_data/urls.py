from django.urls import path
from . import views

urlpatterns=[
    path('webdata',views.MyWebData.as_view(),name='webdata_get_post'),
    path('webdata/<int:pk>/',views.MyWebData_Detail.as_view(),name='webdata_update_delete'),

]
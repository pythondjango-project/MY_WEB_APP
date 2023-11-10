from django.shortcuts import render

from .models import WebData
from rest_framework import generics,viewsets,routers,status
from .serializers import WebDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User


# Create your views here.
'''class WebData_list(generics.ListCreateAPIView):
    queryset = WebData.objects.all()
    serializer_class = WebDataSerializer

class WebData_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WebData.objects.all()
    serializer_class = WebDataSerializer'''

class MyWebData(APIView):
    serializer_class = WebDataSerializer
    def get(self,request):
       #serializers_class = WebDataSerializer
       all_data = WebData.objects.all().values()
       response ={
            "message":"all data fetched succesfully",
            "data":all_data
            }
       return Response(data=response)
    
       
       ''' mydata ={
    "input": [
        {
            "label": "Username",
            "name": "user_name",
            "type": "text"
        },
        {
            "label": "First Name",
            "name": "first_name",
            "type": "text"
        },
        {
            "label": "Last Name",
            "name": "last_name",
            "type": "text"
        },
        {
            "label": "EmailId",
            "name": "email_id",
            "type": "text"
        },
        {
            "label": "Phone Number",
            "name": "phone_number",
            "type": "text"
        },
        {
            "label": "Gender",
            "name": "gender",
            "type": "dropdown",
            "options": [
                "None",
                "Male",
                "Female",
                "Other"
            ]
        }
    ]
}'''
        
    

    def post(self,request):
            serializer = WebDataSerializer(data=request.data)
            if serializer.is_valid():
                 
                WebData.objects.create(username=serializer.data.get("username"),
                                   first_name=serializer.data.get("first_name"),
                                   last_name=serializer.data.get("last_name"),
                                   email_id=serializer.data.get("email_id"),
                                   phone_number=serializer.data.get("phone_number"),
                                   gender=serializer.data.get("gender")
                                   )
                newdata=WebData.objects.all().filter(username=request.data["username"]).values()
                response1= {
                 "messages":"all data added succesfully",
                 "newdata":newdata
            }
            
            return Response(data=response1,status=status.HTTP_201_CREATED)
        




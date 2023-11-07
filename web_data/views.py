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
    def get(self,request):
       
        mydata ={
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
}
        return Response(mydata,status=status.HTTP_200_OK)
    

    def post(self,request):
        serializer = WebDataSerializer(data = request.data)
        print(serializer)
      
        if serializer.is_valid():
            User.objects.create_user(
                username=serializer.validated_data['username'],
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                email_id=serializer.validated_data['email_id'],
                phone_number=serializer.validated_data['phone_number'],
                gender=serializer.validated_data['gender']

            )
            
            return Response({"message":"user registered successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




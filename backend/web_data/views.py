from django.shortcuts import render
from django.http import Http404

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
    
class MyWebData_Detail(APIView):
    def get_object(self, pk): 
        # Returns an object instance that should  be used for detail views. 
        
        try: 
            return WebData.objects.get(pk=pk) 
        except WebData.DoesNotExist: 
            raise Http404 

    def get(self,request,pk,format=None):
         webdata=self.get_object(pk)
         serializer_obj =WebDataSerializer(webdata)
         return Response(serializer_obj.data)
    

    def put(self,request,pk,format=None):
         webdata = self.get_object(pk)
         serializer_obj =WebDataSerializer(webdata,data=request.data)
         if serializer_obj.is_valid():
              serializer_obj.save()
              return Response(serializer_obj.data)
         return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
        

    
    def delete(self,request,pk,format=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response({"message":"data is deleted succesfully"},status=status.HTTP_204_NO_CONTENT)
    
        
        
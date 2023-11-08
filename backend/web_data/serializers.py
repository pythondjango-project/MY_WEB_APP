from rest_framework import serializers
from .models import WebData

class WebDataSerializer(serializers.ModelSerializer):
    class Meta():
        model = WebData
        fields = ["username","first_name","last_name","email_id","phone_number","gender"]
       # fields ='__all__'
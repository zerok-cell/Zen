
from rest_framework import serializers
from django.contrib.auth import get_user_model

class Search(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('username','is_active','photo',)
        

class AddUser(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username','password','email',)
        

class Check(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = "__all__"
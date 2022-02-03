from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from post_app.models import post
from post_app.serializers import PostSerializer
from post_app import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.hashers import make_password
from rest_framework import status





# Create your views for Snacks
class GetOrCreatePost(APIView):
    renderer_classes=[TemplateHTMLRenderer]
    template_name='navbar.html'
    
    def get(self,request):
        post_data=models.post.objects.all()
        post_serialized_data=PostSerializer(post_data,many=True)
        return Response(data={'Data':post_serialized_data.data})
    
    def post(self,request):
        request_data=request.data
        print(request.user)
        post_obj=PostSerializer(data=request_data)
        if post_obj.is_valid():
            post_obj.save()
            return Response(data={'Status':"Saved"},status=201)
        return Response(status=400,data={'Error':post_obj.errors})
        

class GetPutDeletePost(APIView):

    
    def get(self,request,id):
        try:
            post_data=models.post.objects.get(post_id=id)
            post_serialized_data=PostSerializer(post_data)
            return Response(data={'Data':post_serialized_data.data})
        
        except models.post.DoesNotExist:
            return Response(data={'Data':"Not Present"},status=404)
        
    def put(self,request,id):
        request_data=request.data
        try:
            post_data=models.post.objects.get(post_id=id)
            post_serialized_data=PostSerializer(post_data,data=request_data)
            if post_serialized_data.is_valid():
                post_serialized_data.save()
                return Response(data={'Data':post_serialized_data.data})
            return Response(status=400,data={'Error':post_serialized_data.errors})
        except models.post.DoesNotExist:
            return Response(data={'Data':"Not Present"},status=404)
        
    
 
    def delete(self,request,id):
        try:
            post_data=models.post.objects.get(post_id=id)
            post_data.delete()
            return Response(data={'Status':'Deleted'})
        except models.post.DoesNotExist:
            return Response(data={'Data':"Not Present"},status=404)






from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from comment_app.models import comment
from comment_app.serializers import CommentSerializer
from comment_app import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated,AllowAny





# Create your views for Snacks
class GetOrCreateComment(APIView):
    
    def get(self,request):
        comment_data=models.comment.objects.all()
        comment_serialized_data=CommentSerializer(comment_data,many=True)
        return Response(data={'Data':comment_serialized_data.data})
    
    def post(self,request):
        request_data=request.data
        print(request.user)
        comment_obj=CommentSerializer(data=request_data)
        if comment_obj.is_valid():
            comment_obj.save()
            return Response(data={'Status':"Saved"},status=201)
        return Response(status=400,data={'Error':comment_obj.errors})
        

class GetPutDeleteComment(APIView):

    
    def get(self,request,id):
        try:
            comment_data=models.comment.objects.get(comment_id=id)
            comment_serialized_data=CommentSerializer(comment_data)
            return Response(data={'Data':comment_serialized_data.data})
        
        except models.comment.DoesNotExist:
            return Response(data={'Data':"Not Present"},status=404)
        
    def put(self,request,id):
        request_data=request.data
        try:
            comment_data=models.comment.objects.get(comment_id=id)
            comment_serialized_data=CommentSerializer(comment_data,data=request_data)
            if comment_serialized_data.is_valid():
                comment_serialized_data.save()
                return Response(data={'Data':comment_serialized_data.data})
            return Response(status=400,data={'Error':comment_serialized_data.errors})
        except models.comment.DoesNotExist:
            return Response(data={'Data':"Not Present"},status=404)
        
    
 
    def delete(self,request,id):
        try:
            comment_data=models.comment.objects.get(comment_id=id)
            comment_data.delete()
            return Response(data={'Status':'Deleted'})
        except models.comment.DoesNotExist:
            return Response(data={'Data':"Not Present"},status=404)



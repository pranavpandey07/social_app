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
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.hashers import make_password





# Create your views for Snacks
class GetOrCreateComment(APIView):
    renderer_classes=[TemplateHTMLRenderer]
    template_name='dashboard.html'
    
    def get(self,request):
        #renderer_classes=[TemplateHTMLRenderer]
        #template_name='dashboard.html'
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


class LikeView(APIView):
    
    def get(self,request,id):
        try:
            post_data=models.comment.objects.get(comment_id=id)
            post_data.likes_counts=post_data.likes_counts+1
            post_data.save()
            #post_serialized_data=PostSerializer(post_data)
            return Response(data={'Data':"Liked the Comment!!"})
        
        except models.comment.DoesNotExist:
            return Response(data={'Data':"Not Present"},status=404)

class DislikeView(APIView):
    
    def get(self,request,id):
        try:
            post_data=models.comment.objects.get(comment_id=id)
            post_data.dislikes_count=post_data.dislikes_count+1
            post_data.save()
            #post_serialized_data=PostSerializer(post_data)
            return Response(data={'Data':"Disliked the Comment!!"})
        
        except models.comment.DoesNotExist:
            return Response(data={'Data':"Not Present"},status=404)




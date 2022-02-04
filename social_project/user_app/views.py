import email
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from user_app.models import user
from user_app.serializers import UserSerializer
from user_app import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.hashers import make_password,check_password
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.hashers import make_password






# Create your views for Snacks
class GetOrCreateUser(APIView):
    renderer_classes=[TemplateHTMLRenderer]
    template_name='dashboard.html'
    
    def get(self,request):
        user_data=models.user.objects.all()
        user_serialized_data=UserSerializer(user_data,many=True)
        return Response(data={'Data':user_serialized_data.data})
    
    def post(self,request):
        request_data=request.data
        print(request.user)
        user_obj=UserSerializer(data=request_data)
        if user_obj.is_valid():
            user_obj.save()
            return Response(data={'Status':"Saved"},status=201)
        return Response(status=400,data={'Error':user_obj.errors})
        

class GetPutDeleteUser(APIView):

    
    def get(self,request,id):
        try:
            user_data=models.user.objects.get(user_id=id)
            user_serialized_data=UserSerializer(user_data)
            return Response(data={'Data':user_serialized_data.data})
        
        except models.user.DoesNotExist:
            return Response(data={'Data':"Not Present"},status=404)
        
    def put(self,request,id):
        request_data=request.data
        try:
            user_data=models.user.objects.get(user_id=id)
            user_serialized_data=UserSerializer(user_data,data=request_data)
            if user_serialized_data.is_valid():
                user_serialized_data.save()
                return Response(data={'Data':user_serialized_data.data})
            return Response(status=400,data={'Error':user_serialized_data.errors})
        except models.user.DoesNotExist:
            return Response(data={'Data':"Not Present"},status=404)

    def patch(self,request,id):
        request_data=request.data
        try:
            user_data=models.user.objects.get(user_id=id)
            user_serialized_data=UserSerializer(user_data,data=request_data,partial=True)
            if user_serialized_data.is_valid():
                user_serialized_data.save()
                return Response(data={'Data':user_serialized_data.data})
            return Response(status=400,data={'Error':user_serialized_data.errors})
        except models.user.DoesNotExist:
            return Response(data={'Data':"Not Present"},status=404)
        
    
 
    def delete(self,request,id):
        try:
            user_data=models.user.objects.get(user_id=id)
            user_data.delete()
            return Response(data={'Status':'Deleted'})
        except models.user.DoesNotExist:
            return Response(data={'Data':"Not Present"},status=404)



'''class SignupView(APIView):
    def post(self,request):

        data = request.data
        try:
            user =models.user.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                mobile_num=data['mobile_num'],
                email=data['email'],
                password=make_password(data['password']),
                address=data['address'],
                state=data['state'],
                country=data['country'],
                zip_code=data['zip_code']
               
            )

            serializer = UserSerializer(user, many=False)
            return Response(serializer.data)
        except:
            message = {'detail': 'User with this email already exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)'''

class LoginUser(APIView):
    
    
    def post(self,request):
        request_data=request.data
        print(request_data)
        print(request_data['email'])
        print(request_data['password'])
        print("########******")
        try:
            user=models.user.objects.get(email=request_data['email'])
            
            print(user.password)
            if user.password==request_data['password']:
                print("Correct Password!!!")
                print(request_data)
                token,created=Token.objects.get_or_create(user=user)
                return Response({"Token":token.key,"Data" : "Great!!!! You are logged in"})
            else:
                print("Wrong Password")
                return Response(data={"Data":"Bad Password"})

        except models.user.DoesNotExist:
            return Response(data={'Data':"Such user does not exist"},status=404)


class LogOut(APIView):

    def post(self,request):
        #user=models.user.objects.get(email=request_data['email'])
        logout(request)
        return Response(data={"Data: Session logged out"})

class ChangePassword(APIView):

    def post(self,request):
        request_data=request.data
        print(request_data)
        u=user.objects.get(email=request_data["email"])
        u.set_password(request_data["password"])
        u.save()
        return Response(data={"Data":"Password Changed"})
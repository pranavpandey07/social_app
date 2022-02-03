from django.urls import path
from user_app import views

urlpatterns = [
   
    path('user/',views.GetOrCreateUser.as_view()),
    path('user/<int:id>/',views.GetPutDeleteUser.as_view()),
    path('user/login/',views.LoginUser.as_view()),
    path('user/logout/',views.LogOut.as_view()),
    path('user/change_password/',views.ChangePassword.as_view())
]
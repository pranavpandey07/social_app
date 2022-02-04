from django.urls import path
from user_app import views

urlpatterns = [
   
    path('user/',views.GetOrCreateUser.as_view(),name="dashboard"),
    path('user/<int:id>/',views.GetPutDeleteUser.as_view()),
    path('user/login/',views.LoginUser.as_view(),name="login"),
    path('user/logout/',views.LogOut.as_view(),name='logout'),
    path('user/change_password/',views.ChangePassword.as_view())
]
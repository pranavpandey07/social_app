from django.urls import path
from post_app import views

urlpatterns = [
   
    path('post/',views.GetOrCreatePost.as_view(),name='homepage'),
    path('post/<int:id>/',views.GetPutDeletePost.as_view()),
    
]
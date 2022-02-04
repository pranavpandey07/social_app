from django.urls import path
from post_app import views

urlpatterns = [
   
    path('post/',views.GetOrCreatePost.as_view(),name='homepage'),
    path('post/<int:id>/',views.GetPutDeletePost.as_view()),
    path('post/like/<int:id>/',views.LikeView.as_view(),name="like"),
    path('post/dislike/<int:id>/',views.DislikeView.as_view(),name='dislike'),
    path('post/share/<int:id>/',views.ShareView.as_view(),name="share")
    
]
from django.urls import path
from comment_app import views

urlpatterns = [
   
    path('comment/',views.GetOrCreateComment.as_view(),name='dashboard'),
    path('comment/<int:id>/',views.GetPutDeleteComment.as_view(),name="comment"),
    path('comment/like/<int:id>/',views.LikeView.as_view()),
    path('comment/dislike/<int:id>/',views.DislikeView.as_view())
]
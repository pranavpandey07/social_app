from django.urls import path
from comment_app import views

urlpatterns = [
   
    path('comment/',views.GetOrCreateComment.as_view()),
    path('comment/<int:id>/',views.GetPutDeleteComment.as_view())
]
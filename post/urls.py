from django.urls import path

from . import views

urlpatterns = [
    # path('createpost/', views.CreateNewPost.as_view(), name='createpost'),
   path('postlist/', views.PostListView.as_view(), name='post_list')
]

from django.urls import path
from .views import  PostListView,PostCreateView
from django.conf.urls import url
from . import views


urlpatterns=[
    path('',PostListView.as_view(), name='home'),
    # path('user/<str:username>/', UserProjectListView.as_view(), name='user-projects'),
    url(r'^like/(\d+)',views.likePost, name="likePost"),  
    path('profile/update/',views.profile_update, name="profile-update"),
    path('profile/', views.profile, name='profile'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]
from.import views
from django.urls import path, include

urlpatterns = [
  path('', views.PostList, name = 'home'),
  path('<slug:slug>', views.PostDetail, name = 'post_detail'),
]


from django.urls.resolvers import URLPattern

from django.urls import path
from . import views

urlpatterns = [
    path('',views.Root.as_view()),
    path('api/v1/blogs/', views.Blogs.as_view()),
    path('api/v1/blogs/<int:id>/',views.BlogDetails.as_view())
]
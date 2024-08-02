"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog.views import (blog_post, blog_posts, blog_posts1,
                        blog_post_error, passes_test, passes_test_group,
                        blog_posts2, blog_posts3)
from website.views import home, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blog/', blog_post, name='blog-index'),
    path('blog/articles/', blog_posts2, name='articles'),
    path('blog/error/', blog_post_error, name='error'),
    path('blog/test/', passes_test, name='passes_test'),
    path('blog/test/group', passes_test_group, name='passes_test_group'),
    path('blog/<int:pk>/', blog_posts, name='blog_pk'),
    path('blog/<str:slug>/', blog_posts1, name='blog-post1'),
    path('blog/article/<str:slug>/', blog_posts3, name='blog3'),
    path('signup/', signup, name='form'),
]

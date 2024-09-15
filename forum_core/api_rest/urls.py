"""
URL configuration for forum_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from .api_views.forum_api_view import ForumViewSet
from .api_views.subject_api_view import SubjectViewSet
from .api_views.message_api_view import MessageViewSet



router = routers.DefaultRouter()
router.register(r'forums',ForumViewSet)
router.register(r'subjects',SubjectViewSet)
router.register(r'messages',MessageViewSet)




urlpatterns = [
    path('', include(router.urls)),

]


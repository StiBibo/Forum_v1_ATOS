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
from django.urls import path
from .api_views.forum_api_view import list_forum, forum_detail
from .api_views.subject_api_view import list_subject, subject_detail
from .api_views.message_api_view import list_message


app_name = 'api'

urlpatterns = [

    # Forum operations 
    path('list_forum/', list_forum, name='list_forum'),
    path('detail_forum/<int:id>/', forum_detail, name='detail_forum'),

    # Message operations
    path('list_message/', list_message, name='list_message'),

    # Subject operations
    path('list_subject/', list_subject, name='list_subject'),
    path('subject_detail/<int:id>/', subject_detail, name='subject_detail'),


]

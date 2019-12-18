"""critic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path , include
from . import views

app_name = 'message'

urlpatterns = [
    path('home/',views.home_view,name='home'),
    path('create/<str:user_2>/',views.create_view,name='create'),# safe as it call user one authenticity and only connects to other
    path('message/', views.message_view, name = 'message'),
    path('detail/<str:messageid>/',views.messagedetail_view,name='detail'),  # safe give the conversation
    path('chat/<str:messageid>',views.chat_view, name="chat"), # safe redirect to detail after adding message
    path('',views.animation_view,name="animation"),
    path('warning/<str:messageheader>/<str:message>/',views.warning_view,name="warning"),
    path('messageBlock/<str:messageid>/',views.messageBlock_view,name="messageBlock"),#safe render convo in message detail
    path('profile/',views.profile_view,name="profile"),
]

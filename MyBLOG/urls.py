"""MyBLOG URL Configuration

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
from django.urls import path
# from .views import *
# from MyBlog.views import *
from BLOGAPP.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",Homepage),
    # path("view/",viewpage),
    # path('Detail/',Detailpage),
    # path("allevent/",All),
    # path("pages/<int:a>/",page),
    # path("one/",Onefun),
    path("",Homepage),
    path("CreateTable/",CreateTable),
    path("Ctable/",CTable),
    path("Title/<int:a>/",ContainPage),
    path("Login/",Login_page),
    path("Login_data/",LGdata),
    path("logout/",Logout),
    path('About/',AboutPage),
    path('policy/',Policy),
    path('contact/',Contact),
]


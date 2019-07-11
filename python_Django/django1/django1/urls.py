"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from FirstApp import views 
from TimeApp import views as v2
from greetingsApp import views as v3
from GreetingImg import views as v4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome_django),
    path('date/',v2.date_display),
    path('greet/',v3.greet_display),
    path('greet1/',v4.greet_disp),
    path('bankapp/',include('BankApp.urls')),
]

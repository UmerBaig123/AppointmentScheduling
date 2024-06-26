"""
URL configuration for appointment_scheduling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import threading
from django.contrib import admin
from django.urls import path,include
from home.views import islView,checkAvailability,home,krView
from home.utils import get_appointment_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('login.urls')),
    path('', home, name='home'),
    path('isl/', islView, name='islamabad'),
    path('kr/', krView, name='karachi'),
    path('checkavailability/', checkAvailability.as_view(), name='checkavailability'),
]
search_thread = threading.Thread(target=get_appointment_url,name="geturl", args=())
search_thread.start()
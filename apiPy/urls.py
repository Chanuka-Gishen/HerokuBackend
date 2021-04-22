"""apiPy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weburl/', include('weburl.urls')),
    path('lankaProperty/', include('weburl.urls')),
    path('ikmanlk/', include('weburl.urls')),
    path('ceylonLanka/', include('weburl.urls')),
    path('valuate/', include('valuate.urls')),
    path('city/<city>', include('valuate.urls')),
    path('export_csv/', include('valuate.urls')),
    path('user/', include('user.urls')),
    path('addnewuser/', include('user.urls')),
    path('getusers/', include('user.urls')),
    path('loancal/', include('user.urls')),
    path('auth/', obtain_auth_token),
    path('give_predictions/', include('user.urls')),
    path('get_valuate_inputs/', include('valuate.urls')),
    path('get_data/', include('valuate.urls')),
    path('generated_result/', include('valuate.urls')),
]

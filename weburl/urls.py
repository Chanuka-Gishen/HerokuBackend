from apiPy.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lankaProperty/', views.getLankaProperty, name="lankaproperty"),
    path('ikmanlk/', views.getIkmanLk, name="ikmanlk"),
    path('ceylonLanka/', views.getCeylonProperty),
]

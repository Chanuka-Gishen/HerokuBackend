from apiPy.urls import path
from . import views

urlpatterns = [
    path('addnewuser/',views.addUserApi),
    path('getusers/', views.getusers),
    path('loancal/', views.loancalculator),
]
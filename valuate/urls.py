from apiPy.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('city/<city>', views.getCity, name="city"),
    path('export_csv/', views.export_csv),
    path('give_predictions/', views.give_predictions),
    path('get_valuate_inputs/', views.get_valuate_inputs),
]
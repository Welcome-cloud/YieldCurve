from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('plot/', views.yield_curve_by_date, name='plot'),
]


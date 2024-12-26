from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('plot/', views.yield_curve_plot, name='yield_curve_plot'),
    path('plot/<str:selected_date>/', views.yield_curve_by_date, name='yield_curve_by_date'),
]


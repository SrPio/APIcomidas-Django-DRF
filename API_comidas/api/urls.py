
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_plato, name='add_platos'),
    path('crear/', views.create, name='create'),
    path('all/', views.view_platos, name='view_platos'),
    path('update/<int:pk>/', views.update_platos, name='update-platos'),
    path('item/<int:pk>/delete/', views.delete_platos, name='delete-platos'),
]
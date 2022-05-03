
from django.urls import include, path
from . import views
from rest_framework import routers

from api.views import PlatosViewSet

router = routers.DefaultRouter()
router.register(r'plato', PlatosViewSet, basename='plato')


urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('all/', views.view_platos, name='view_platos'),
    path('create/', include(router.urls)),
    path('update/<int:pk>/', views.update_platos, name='update-platos'),
    path('plato/<int:pk>/delete/', views.delete_platos, name='delete-platos'),
]
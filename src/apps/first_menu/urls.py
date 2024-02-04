from django.urls import path
from .views import get_menu, base

urlpatterns = [
    path('', base, name='base'),
    path('<path:path>/', get_menu, name='get_menu'),
]

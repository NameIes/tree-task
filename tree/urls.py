from django.urls import path

from .views import index, menu

urlpatterns = [
    path('', index),
    path('<int:menu_id>/', menu),
    path('<int:menu_id>/<path:path>', menu),
]

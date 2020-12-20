from django.urls import path, include

from rest_framework import routers

from . import views

api = routers.DefaultRouter()
api.register('',views.BoardViewSet)

urlpatterns = [
    path('', include(api.urls)),
]
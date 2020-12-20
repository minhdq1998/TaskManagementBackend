from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from .models import Board
from .serializers import BoardSerializer

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all().order_by('modified')
    serializer_class = BoardSerializer
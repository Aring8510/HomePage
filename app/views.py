from django.db.models import query
from django.shortcuts import render
from ping3 import ping
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Target
from .serializer import TargetSerializer

def index(request):
    result = ping('192.168.11.1')
    print(result)

    return render(request, 'index.html', {})
def healthCheck(request, pk):

    return render(request, 'index.html', {})

class Targets(viewsets.ModelViewSet):
    serializer_class = TargetSerializer
    queryset = Target.objects.all()
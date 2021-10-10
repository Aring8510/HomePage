from django.db.models import query
from django.shortcuts import render
from django.http.response import JsonResponse
from ping3 import ping
from rest_framework import generics, viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Target, Blog
from .serializer import BlogSerializer, TargetSerializer

def index(request):
    return render(request, 'index.html', {})

@api_view(['GET'])
def healthCheck(request, pk):
    target = Target.objects.get(id=pk)
    health = ping(target.host)
    result = {'health' : health}
    return Response(result)

class Targets(viewsets.ModelViewSet):
    serializer_class = TargetSerializer
    queryset = Target.objects.all()

class getOneTarget(generics.RetrieveAPIView):
    serializer_class = TargetSerializer
    queryset = Target.objects.all()
    lookup_field = 'pk'


class Blogs(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

class getOneBlog(generics.RetrieveAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field = 'pk'

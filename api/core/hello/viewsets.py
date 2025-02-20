from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

class Hello(viewsets.ViewSet):
    http_method_names = ["get"]
    renderer_classes = [JSONRenderer] 

    def list(self, request):
        """Return a hello message"""
        return Response({"message": "Hello!"})

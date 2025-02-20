from rest_framework import status, viewsets
from rest_framework.response import Response
from core.summarize.serializers import SummarizeSerializer
from core.summarize.summarizer.summarizer import summarizer

import asyncio

class SummarizeViewSet(viewsets.ViewSet):
    http_method_names = ["post"]

    def create(self, request):
        """Handles POST requests for text summarization."""
        serializer = SummarizeSerializer(data=request.data) 

        if serializer.is_valid():
            url = serializer.validated_data["url"]
            summarized_data = asyncio.run(summarizer(url))
            print(summarized_data)
            return Response({
                "status": "success",
                "summarized_data": summarized_data
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import serializers


class SummarizeSerializer(serializers.Serializer):
    url = serializers.URLField()

    def validate(self, data):
        return data                                                                                                                                                                                                              

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status


class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hellow orld"}, status=status.HTTP_200_OK)
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status


class HelloOrderView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello orders world"}, status=status.HTTP_200_OK)
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import  status

from .serializers import PlotSerializer
from .models import Plot
from .permissions import IsOwner

# Create your views here.

class PlotView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        """Create a Plot"""

        request.data['owner'] = request.user.id

        serializer = PlotSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, format=None):
        """List of plots for a user"""
        plots = Plot.objects.filter(owner=request.user.id)
        serializer = PlotSerializer(plots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PlotDetailView(APIView):

    permission_classes = (IsAuthenticated, IsOwner)

    def delete(self, request, pk=None, format=None):
        """Delete a plot"""
        plot = get_object_or_404(Plot.objects.all(), pk=pk)
        self.check_object_permissions(request, plot)
        plot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk=None, format=None):
        """Update a plot"""
        plot = get_object_or_404(Plot.objects.all(), pk=pk)
        self.check_object_permissions(request, plot)
        request.data['owner'] = request.user.id
        serializer = PlotSerializer(plot, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


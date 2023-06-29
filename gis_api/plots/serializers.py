from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Plot

class PlotSerializer(serializers.ModelSerializer):
    area = serializers.SerializerMethodField()

    class Meta:
        model = Plot
        fields = '__all__'
        read_only_fields = ('id', 'area')

        extra_kwargs = {
            'owner': {'write_only': True}
        }

    def get_area(self, obj):
        return obj.geometry.area

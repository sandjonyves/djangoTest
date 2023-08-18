from rest_framework import serializers

from .models import DataReact

class DataSerializers(serializers.ModelSerializer):
    class Meta:
        model = DataReact
        fields = ('id','name','niveau', 'classe')
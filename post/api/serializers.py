from rest_framework.serializers import ModelSerializer
from post.models import Post, Vehiculo

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','content']

class VehiculoSerializer(ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = [
            'Anno',
            'Marca',
            'Color',
            'Combustible',
            'NumPuertas',
            'Traccion'
        ]
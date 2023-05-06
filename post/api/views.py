from rest_framework.viewsets import ModelViewSet
from post.models import Post, Vehiculo
from post.api.serializers import PostSerializer, VehiculoSerializer

# Create your views here.

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class VehiculoApiViewSet(ModelViewSet):
    serializer_class = VehiculoSerializer
    queryset = Vehiculo.objects.all()

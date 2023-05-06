from rest_framework.routers import DefaultRouter
from post.api.views import PostApiViewSet ,VehiculoApiViewSet

router_post = DefaultRouter()

router_post.register(prefix='vehiculo', basename='vehivulo', viewset=VehiculoApiViewSet)
router_post.register(prefix='post', basename='post', viewset=PostApiViewSet)
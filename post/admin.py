from django.contrib import admin
from post.models import Post,Vehiculo

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    lis_display = ['id', 'title']

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = [            
            'Anno',
            'Marca',
            'Color',
            'Combustible',
            'NumPuertas',
            'Traccion']
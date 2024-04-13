from django.contrib import admin

# Register your models here.


from .models import Marca, Acessorio, Categoria, Cor

admin.site.register(Marca)
admin.site.register(Acessorio)
admin.site.register(Categoria)
admin.site.register(Cor)
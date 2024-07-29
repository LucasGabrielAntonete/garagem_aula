from rest_framework.viewsets import ModelViewSet

from core.garagem.models import Categoria
from core.garagem.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
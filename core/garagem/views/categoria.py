from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.garagem.models import Categoria
from core.garagem.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]
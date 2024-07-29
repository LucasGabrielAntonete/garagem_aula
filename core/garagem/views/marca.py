from rest_framework.viewsets import ModelViewSet

from core.garagem.models import Marca
from core.garagem.serializers import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
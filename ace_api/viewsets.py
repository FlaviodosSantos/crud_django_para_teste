from rest_framework.viewsets import ModelViewSet
from .serializer import AceSerializer
from .models import Ace


class AceViewSet(ModelViewSet):
    # para pegar todos os objetos
    # queryset = Ace.objects.all()

    # para pegar somente os ativos
    queryset = Ace.objects.filter(is_active=True)
    serializer_class = AceSerializer

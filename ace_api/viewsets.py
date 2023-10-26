from rest_framework.viewsets import ModelViewSet
from .serializer import AceSerializer
from .models import Ace
from django.shortcuts import redirect
from rest_framework import generics, mixins


class AceViewSet(ModelViewSet):
    # para pegar todos os objetos
    # queryset = Ace.objects.all()

    # para pegar somente os ativos
    queryset = Ace.objects.filter(is_active=True)
    serializer_class = AceSerializer

    # sobrescreve o DELETE e so muda o is_ative pra False
    def destroy(self, request, *args, **kwargs):
        ace = self.get_object()
        ace.is_active = False
        ace.save()

        # return http.HttpResponseRedirect(redirect_to='ace-list')
        return redirect('/api/v1/')


# listar todos, inclusive is_active = False
class AceListAllViewSet(ModelViewSet):
    queryset = Ace.objects.all()
    serializer_class = AceSerializer

#


class AceRestoreViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Ace.objects.all()
    serializer_class = AceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        ace = self.get_object()
        ace.is_active = True
        ace.save()
        return redirect('/api/v1/')

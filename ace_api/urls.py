from django.urls import path, include
from rest_framework import routers
from ace_api.viewsets import AceViewSet, AceListAllViewSet, AceRestoreViewSet
from ace_api.views import indice, mapa_dengue_caico, AceList

router = routers.DefaultRouter()
router.register(r'ace', AceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list', AceListAllViewSet.as_view({'get': 'list'}), name='list'),
    path('restore/<int:pk>/', AceRestoreViewSet.as_view(), name='restore'),
    path('index', AceList.as_view(), name='index'),
    path('indice/<int:ciclo>/', indice, name='indice'),
    path('mapa/<int:ciclo>', mapa_dengue_caico, name='mapa'),
]

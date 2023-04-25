from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import *

router = SimpleRouter()
router.register('localites', LocaliteModelViewSet, basename='localites')
router.register('categoriecims', CategorieCimetiereModelViewSet, basename='categoriecims')
router.register('defunts', DefuntModelViewSet, basename='defunts')
router.register('cimetieres', CimetiereModelViewSet, basename='cimetieres')
router.register('tombes', TombeModelViewSet, basename='tombes')

urlpatterns = [
    path('root/', include(router.urls)),
]
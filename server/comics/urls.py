from rest_framework.routers import DefaultRouter
from server.comics.views import ComicUniverseViewSet, HeroViewSet

router = DefaultRouter()
router.register(prefix='universe', viewset=ComicUniverseViewSet)
router.register(prefix='heroes', viewset=HeroViewSet)


urlpatterns = router.urls

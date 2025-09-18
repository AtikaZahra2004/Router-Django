from rest_framework import routers
from .views import StudentViewSet

# router = routers.SimpleRouter()
# router.register(r'Student', StudentViewSet)
# urlpatterns = router.urls


from app.views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', StudentViewSet, basename='Student')
urlpatterns = router.urls
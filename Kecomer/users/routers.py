from rest_framework.routers import DefaultRouter

from users.genericviews import ClientViewSet

router = DefaultRouter()
router.register(r'user', ClientViewSet, basename='user')

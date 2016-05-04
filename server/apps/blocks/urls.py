from rest_framework.routers import DefaultRouter
from .viewsets import (FlatBlockViewSet, )

router = DefaultRouter()
router.register(r'flatblocks', FlatBlockViewSet)


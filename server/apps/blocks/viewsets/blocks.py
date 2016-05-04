from flatblocks.models import FlatBlock
from rest_framework import mixins
from rest_framework import viewsets


from .permissions import BlockPermission
from ..serializers import CreateFlatBlockSerializer, ReadOnlyFlatBlockSerializer


class FlatBlockViewSet(mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    permission_classes = (BlockPermission,)
    queryset = FlatBlock.objects.all()

    def perform_create(self, serializer):
        serializer.save(use_for_migrations=True)

    def perform_update(self, serializer):
        serializer.save(use_for_migrations=True)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return CreateFlatBlockSerializer
        return ReadOnlyFlatBlockSerializer

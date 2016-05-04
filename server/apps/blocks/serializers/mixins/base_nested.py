from copy import copy
from collections import OrderedDict

from rest_framework import serializers

from .dynamic_fields import DynamicFieldsMixin


class BaseNestedSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # TODO: Find better solution for this
        # Copy ignore creation for future manipulations
        self._ignore_creation = copy(getattr(self.Meta, 'ignore_creation', ()))
        super(BaseNestedSerializer, self).__init__(*args, **kwargs)

    @staticmethod
    def get_sorted_by_create_priority(items):
        # Sort items by create priority param if `CreatePriorityMixin` is used
        return OrderedDict(
            sorted(
                items.items(),
                key=lambda item: getattr(item[1], '_create_priority', 0)
            )
        )

    def _get_kwargs_for_serializer(self, serializer):
        kwargs = {}
        if isinstance(serializer, DynamicFieldsMixin):
            kwargs = {
                'fields': [field for field in serializer.fields.keys()],
            }
        return kwargs

    def _get_new_serializer(self, serializer, **kwargs):
        kwargs.update(self._get_kwargs_for_serializer(serializer))
        kwargs.update({
            'context': self.context
        })
        return serializer.__class__(**kwargs)

    def call_after_saved_callback(self, instance, field_name):
        method = getattr(self, 'after_{}_saved'.format(field_name), None)
        if callable(method):
            method(instance)

    def after_reverse_relations_saved(self, instance):
        pass

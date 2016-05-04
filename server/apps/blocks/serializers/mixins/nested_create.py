from collections import OrderedDict
from rest_framework import serializers
from .base_nested import BaseNestedSerializer


class NestedCreateMixin(BaseNestedSerializer):
    """
    Mixin adds nested create feature.
    Before use set Meta param `nested_related_kwarg` that will be set on
    reverse relations. This param is need for set foreign key of reverse
    relations to this model.
    For ignore creation of some fields use Meta param `ignore_creation` with
    tuple of field names, that will be skipped
    TODO: in future find this field automatically based on model foreign key
    fields
    """
    def create(self, validated_data):
        reverse_relations = OrderedDict()
        relations = OrderedDict()

        # Sort fields by create priority
        fields = self.get_sorted_by_create_priority(self.fields)
        # Remove related fields from validated data for future manipulations
        for field_name, field in fields.items():
            if field.read_only or field_name in self._ignore_creation:
                continue

            if isinstance(field, serializers.ListSerializer):
                if isinstance(field.child, serializers.ModelSerializer):
                    if validated_data.pop(field.source, None) is None:
                        # Skip field if field is not required or null allowed
                        continue
                    reverse_relations[field_name] = field.child

            if isinstance(field, serializers.ModelSerializer):
                if validated_data.pop(field.source, None) is None:
                    # Skip field if field is not required or null allowed
                    continue
                relations[field_name] = field

        nested_related_kwarg = getattr(self.Meta, 'nested_related_kwarg', None)
        if reverse_relations:
            assert nested_related_kwarg, \
                "Set `nested_related_kwarg` in Meta options for use nested " \
                "create feature"

        # Create direct relations (foreign key)
        for field_name, field in relations.items():
            serializer = self._get_new_serializer(
                field, data=self.initial_data[field_name])
            serializer.is_valid(raise_exception=True)
            validated_data[field.source] = serializer.save()

        # Create instance
        instance = super(NestedCreateMixin, self).create(validated_data)
        if reverse_relations:
            self.create_reverse_relations(instance, reverse_relations)

        return instance

    def create_reverse_relations(self, instance, reverse_relations):
        # Create reverse relations (many to one)
        nested_related_kwarg = getattr(self.Meta, 'nested_related_kwarg')

        for field_name, field in reverse_relations.items():
            save_kwargs = {nested_related_kwarg: instance}
            for data in self.initial_data[field_name]:
                serializer = self._get_new_serializer(field, data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save(**save_kwargs)
            self.call_after_saved_callback(instance, field_name)
        self.after_reverse_relations_saved(instance)

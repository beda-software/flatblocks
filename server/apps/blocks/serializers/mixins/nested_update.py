from collections import OrderedDict
from rest_framework import serializers
from .base_nested import BaseNestedSerializer
from django.db.models import ProtectedError


class NestedUpdateMixin(BaseNestedSerializer):
    default_error_messages = {
        'cannot_delete_protected': "Cannot delete {instances} because "
                                     "protected relation is exists"
    }

    def update(self, instance, validated_data):
        reverse_relations = OrderedDict()
        relations = OrderedDict()

        # Sort fields by create priority
        fields = self.get_sorted_by_create_priority(self.fields)
        # Remove related fields from validated data for future manipulations
        for field_name, field in fields.items():
            if field.read_only:
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

        if relations:
            raise NotImplementedError("NestedUpdateMixin not provide update "
                                      "for direct relations")

        # Update instance
        instance = super(NestedUpdateMixin, self).update(
            instance, validated_data)

        if reverse_relations:
            self.update_reverse_relations(instance, reverse_relations)
            self.delete_reverse_relations_if_need(instance, reverse_relations)
        return instance

    def update_reverse_relations(self, instance, reverse_relations):
        # Update reverse relations (many to one)
        nested_related_kwarg = getattr(self.Meta, 'nested_related_kwarg')
        for field_name, field in reverse_relations.items():
            Model = field.Meta.model
            # Prefetch related instances
            instances = Model.objects.filter(
                pk__in=[
                    d.get('pk')
                    for d in self.initial_data[field_name]
                    if d.get('pk', None)
                ])
            instances = {
                related_instance.pk: related_instance
                for related_instance in instances
            }
            for data in self.initial_data[field_name]:
                is_new = data.get('pk') is None
                if is_new:
                    serializer = self._get_new_serializer(field, data=data)
                else:
                    pk = data.get('pk')
                    obj = instances[pk]
                    serializer = self._get_new_serializer(
                        field, instance=obj, data=data)

                save_kwargs = {nested_related_kwarg: instance}
                serializer.is_valid(raise_exception=True)
                related_instance = serializer.save(**save_kwargs)
                if is_new:
                    data['pk'] = related_instance.pk

            self.call_after_saved_callback(instance, field_name)
        self.after_reverse_relations_saved(instance)

    def delete_reverse_relations_if_need(self, instance, reverse_relations):
        nested_related_kwarg = getattr(self.Meta, 'nested_related_kwarg')
        # Reverse `reverse_relations` for correct delete priority
        reverse_relations = OrderedDict(
            reversed(list(reverse_relations.items())))

        # Delete instances which is missed in data
        for field_name, field in reverse_relations.items():
            Model = field.Meta.model
            current_ids = [d.get('pk') for d in self.initial_data[field_name]]

            try:
                Model.objects.filter(
                    **{nested_related_kwarg: instance}
                ).exclude(pk__in=current_ids).delete()
            except ProtectedError as e:
                instances = e.args[1]
                self.fail('cannot_delete_protected', instances=", ".join([
                    instance.__str__() for instance in instances]))

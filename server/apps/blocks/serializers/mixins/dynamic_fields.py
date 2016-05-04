from rest_framework import serializers


class DynamicFieldsMixin(serializers.Serializer):
    """
    A Serializer mixin that takes an additional `exclude` and `fields`
    arguments that controls which fields should be allowed.
    """

    def __init__(self, *args, **kwargs):
        exclude = kwargs.pop('exclude', [])
        fields = kwargs.pop('fields', [])
        # Instantiate the superclass without `exclude` and `fields`
        super(DynamicFieldsMixin, self).__init__(*args, **kwargs)

        if fields:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if exclude:
            for field_name in exclude:
                self.fields.pop(field_name)

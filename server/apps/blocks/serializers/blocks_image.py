from rest_framework import serializers

from ..models import BlockImage


class BlockImageSerializer(serializers.ModelSerializer):
    origin_file_url = serializers.CharField(
        source='image.full_url',
        read_only=True
    )

    class Meta:
        model = BlockImage
        fields = ('origin_file_url', 'preview_file_url', 'cropped_file_url',
                  'cropped_file_url',  'modifier')

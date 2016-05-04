from django.utils.html import linebreaks
from rest_framework import serializers
from flatblocks.models import FlatBlock

from .blocks_image import BlockImageSerializer


class ReadOnlyFlatBlockSerializer(serializers.ModelSerializer):
    images = BlockImageSerializer(many=True, source='blockimage_set')
    header = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    file = serializers.FileField(
        use_url=False
    )
    file_url = serializers.CharField(
        source='file.full_url',
        read_only=True
    )

    def get_header(self, obj):
        if obj.set_linebreaks:
            return linebreaks(obj.header)[3:-4]
        else:
            return obj.header

    def get_content(self, obj):
        if obj.set_linebreaks:
            return linebreaks(obj.content)[3:-4]
        else:
            return obj.content

    class Meta:
        model = FlatBlock
        fields = ('pk', 'slug', 'header', 'content',
                  'file', 'file_url', 'url', 'images')


class CreateFlatBlockSerializer(serializers.ModelSerializer):
    file = serializers.CharField(
        allow_null=True,
        allow_blank=True,
        required=False
    )
    file_url = serializers.CharField(
        source='file.full_url',
        read_only=True
    )

    def validate(self, data):
        data = super(CreateFlatBlockSerializer, self).validate(data)
        if 'header' in data:
            data['show_header'] = bool(data['header'])
        if 'content' in data:
            data['show_content'] = bool(data['content'])
        if 'url' in data:
            data['show_url'] = bool(data['url'])
        if 'file' in data:
            data['show_file'] = bool(data['file'])
        return data

    class Meta:
        model = FlatBlock
        fields = ('pk', 'slug', 'header', 'content',
                  'file', 'file_url', 'url',)

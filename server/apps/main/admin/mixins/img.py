class ImgMixin(object):
    def img_tag(self, obj):
        if obj:
            return '<img src="{}" width="150">'.format(obj.image.url)
        else:
            return ''

    img_tag.short_description = 'Изображение'
    img_tag.allow_tags = True

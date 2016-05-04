from django.contrib import admin

from apps.main.admin.mixins import (ImgMixin, )
from ..models import (BlockImage, )


class BlockImageAdminInLine(ImgMixin, admin.TabularInline):
    model = BlockImage
    readonly_fields = ('img_tag',)
    extra = 1

    fieldsets = (
        ('', {
            'fields': ('image', 'img_tag', 'modifier',),
        }),
    )

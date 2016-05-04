from django.contrib import admin
from django import forms
from flatblocks.models import FlatBlock
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .forms import FileWidget
from .block_image import BlockImageAdminInLine


class BlockAdmin(admin.ModelAdmin):
    list_display = ('slug',)
    readonly_fields = ('slug',)
    inlines = (BlockImageAdminInLine,)

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ['show_header', 'show_content',
                        'show_file', 'show_url', 'set_linebreaks',
                        'use_for_migrations']
        if obj:
            if not obj.show_header:
                self.exclude.extend(['header'])

            if not obj.show_content:
                self.exclude.extend(['content'])

            if not obj.show_file:
                self.exclude.extend(['file'])

            if not obj.show_url:
                self.exclude.extend(['url'])

        form = super(BlockAdmin, self).get_form(request, obj=obj, **kwargs)

        if 'header' not in self.exclude:
            form.base_fields['header'].widget = \
                forms.Textarea(attrs={'class': 'vTextField'})

        if 'file' not in self.exclude:
            form.base_fields['file'].widget = FileWidget()

        return form

    def has_delete_permission(self, request, obj=None):
        return False

    def response_change(self, request, obj):
        r = super(BlockAdmin, self).response_change(request, obj)
        if '_continue' in request.POST:
            return r
        else:
            return HttpResponseRedirect(reverse('admin:index'))

admin.site.unregister(FlatBlock)
admin.site.register(FlatBlock, BlockAdmin)

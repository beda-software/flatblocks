from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe


class FileWidget(forms.FileInput):
    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "full_url"):
            full_url = value.full_url
            out = u'<a href="{}">{}</a><br />{} '
            output.append(out.format(full_url, full_url, _(u'Change:')))
        output.append(super(FileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))

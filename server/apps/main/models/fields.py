from django.db.models.fields.files import FieldFile, FileField
from django.conf import settings
from constance import config


class CustomFieldFile(FieldFile):
    @property
    def full_url(self):
        if not self:
            return None

        name = self.name

        if name.startswith('http://') or name.startswith('https://'):
            return name
        elif name.startswith('/'):
            return "{}{}".format(config.FRONTEND_SITE_URL, name)
        else:
            return "{}{}".format(config.BACKEND_SITE_URL, self.url)


class CustomFileField(FileField):
    attr_class = CustomFieldFile

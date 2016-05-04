from django.db import models
from sorl.thumbnail import get_thumbnail
from constance import config

from apps.main.models.fields import CustomFileField


class ImageModifier(object):
    FULL = '_full'
    THIRD = '_third'
    HALF = '_half'
    FOURTH = '_fourth'

    CHOICES = (
        (FULL, '100%'),
        (THIRD, '75%'),
        (HALF, '50%'),
        (FOURTH, '25%'),
    )

    CROPPED_SIZES = {
        FULL: '1068',
        THIRD: '795',
        HALF: '522',
        FOURTH: '249',
    }


class BlockImage(models.Model):
    block = models.ForeignKey(to='flatblocks.FlatBlock', verbose_name="Блок")
    image = CustomFileField(
        verbose_name='Изображение',
        upload_to="block_image/%Y/%m/%d",
    )
    modifier = models.CharField(
        verbose_name='Ориентация',
        choices=ImageModifier.CHOICES,
        default=ImageModifier.FULL,
        max_length=50,
    )

    @property
    def preview_file_url(self):
        return "{}{}".format(
            config.BACKEND_SITE_URL,
            get_thumbnail(self.image, '1920x1080', quality=99).url
        )

    @property
    def cropped_file_url(self):
        size = ImageModifier.CROPPED_SIZES[self.modifier]

        return "{}{}".format(
            config.BACKEND_SITE_URL,
            get_thumbnail(self.image, size, quality=99).url
        )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return str(self.pk)

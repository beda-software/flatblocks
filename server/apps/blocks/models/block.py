from django.db import models
from flatblocks.models import FlatBlock

from apps.main.models.fields import CustomFileField


FlatBlock.add_to_class(
    'show_header', models.BooleanField(
        verbose_name='Показывать заголовок',
        default=False,
    )
)

FlatBlock.add_to_class(
    'show_content', models.BooleanField(
        verbose_name='Показывать содержание',
        default=False,
    )
)

FlatBlock.add_to_class(
    'show_file', models.BooleanField(
        verbose_name='Показывать файл',
        default=False,
    )
)

FlatBlock.add_to_class(
    'show_url', models.BooleanField(
        verbose_name='Показывать URL',
        default=False,
    )
)

FlatBlock.add_to_class(
    'set_linebreaks', models.BooleanField(
        verbose_name='Заменять перенос строки на тег <br />',
        default=True,
    )
)

FlatBlock.add_to_class(
    'url', models.CharField(
        verbose_name='Url',
        max_length=255,
        blank=True, null=True,
    )
)

FlatBlock.add_to_class(
    'file', CustomFileField(
        max_length=255,
        verbose_name='Файл',
        upload_to="flatblocks/%Y/%m/%d",
        blank=True, null=True,
    )
)

FlatBlock.add_to_class(
    'use_for_migrations', models.BooleanField(
        verbose_name='Включать в выгрузку миграции',
        default=False,
    )
)

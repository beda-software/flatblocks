from grappelli.dashboard import modules, Dashboard
from django.apps import apps


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)
        FlatBlock = apps.get_model('flatblocks', 'FlatBlock')

        self.children.append(modules.ModelList(
            title='Главное',
            column=1,
            collapsible=True,
            models=('flatblocks.models.*',)
        ))

        self.children.append(modules.ModelList(
            title='Настройки',
            column=1,
            collapsible=True,
            models=('constance.*',)
        ))

        self.children.append(modules.ModelList(
            title='Пользователи и группы',
            column=1,
            collapsible=True,
            models=('django.contrib.auth.*',)
        ))

import os
import re

from django.conf import settings
from django.template.loader import render_to_string
from django.core.management.base import BaseCommand
from flatblocks.models import FlatBlock


class Command(BaseCommand):
    help = 'Выгрузка флэтблоков из базы в миграции'

    def add_arguments(self, parser):
        parser.add_argument('--all',
                            action="store_true",
                            default=False,
                            help='Inclide all flatblocks into migration')

    def handle(self, *args, **options):
        migration_path = self.get_flatblocks_migration_path()
        prev_name, new_name = self.get_prev_new_migration_names(migration_path)
        migration_content = self.create_migration_content(prev_name,
                                                          options['all'])
        self.create_migration_file(migration_content, migration_path, new_name)

    def get_flatblocks_migration_path(self):
        '''
        Return the full path for migrations of flatblocks
        '''
        flatblock_migration_path = 'apps.blocks.migrations'

        if hasattr(settings, 'MIGRATION_MODULES'):
            flatblock_migration_path = settings.MIGRATION_MODULES.get(
                'flatblocks', flatblock_migration_path)

        flatblock_migration_path = flatblock_migration_path.replace(".", "/")
        flatblock_migration_fp = os.path.join(settings.SERVER_PATH,
                                              flatblock_migration_path)
        return flatblock_migration_fp

    def get_prev_new_migration_names(self, migration_path):
        """
        retrun names of files for last and future migrations
        """
        file_name_pattern = re.compile("^([0-9]{4}).*\.py$")
        file_list = sorted(os.listdir(migration_path))
        migration_names = [i for i in file_list if file_name_pattern.match(i)]

        if '0001_initial.py' not in migration_names:
            raise Exception('There are no initial migration file')

        last_migration_name = migration_names[-1]
        last_migration_number = file_name_pattern.match(last_migration_name)
        try:
            last_migration_number = int(last_migration_number.group(1))
        except ValueError:
            last_migration_number = 1

        new_migration_name = "{:0>4}_data_auto.py".format(
            last_migration_number + 1,
        )

        return last_migration_name, new_migration_name

    def create_migration_content(self, prev_name, all=False):
        flatblock_list = FlatBlock.objects.all()
        if not all:
            flatblock_list = flatblock_list.filter(use_for_migrations=True)

        if not flatblock_list:
            raise Exception('There are no flatblocks for migration')

        for item in flatblock_list:
            item.use_for_migrations = False
            item.save()

        return render_to_string(
            'blocks/migration.html',
            {
                'flatblock_list': flatblock_list,
                'prev_migration_filename': prev_name.replace(".py", ""),
            }
        )

    def create_migration_file(self, content, directory, file_name):
        f = open(os.path.join(directory, file_name), 'w+')
        f.write(content)
        f.close()
        print (file_name)

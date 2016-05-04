from flatblocks.models import FlatBlock
from factory import DjangoModelFactory, Factory, Sequence, django


class BlockFactory(DjangoModelFactory):
    slug = Sequence(lambda n: 'slug%d' % n)

    class Meta:
        model = FlatBlock


class BlockFileFactory(BlockFactory):
    file = django.ImageField(filename='example_image.jpeg', format='jpeg',
                             color='green')

    class Meta:
        model = FlatBlock

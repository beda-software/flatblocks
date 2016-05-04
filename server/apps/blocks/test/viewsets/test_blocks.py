import json
from unittest import skip

from rest_framework.test import APITestCase
from flatblocks.models import FlatBlock

from ...serializers import CreateFlatBlockSerializer
from ...factories import BlockFactory, BlockFileFactory


class BlocksTestCase(APITestCase):
    def setUp(self):
        self.only_header_block = BlockFactory.build(header="header")
        self.only_content_block = BlockFactory.build(content="content")
        self.only_url_block = BlockFactory.build(url="url")
        self.only_file_block = BlockFileFactory.build()
        self.only_header_content_block = BlockFactory.build(
            header="header",
            content="content",
        )

    def test_only_header(self):
        response = self.client.post(
            "/flatblocks/",
            data=json.dumps(
                CreateFlatBlockSerializer(self.only_header_block).data
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)

        block = FlatBlock.objects.get(slug=self.only_header_block.slug)

        self.assertTrue(block.show_header)
        self.assertFalse(block.show_content)
        self.assertFalse(block.show_url)
        self.assertFalse(block.show_file)

    def test_only_content(self):
        response = self.client.post(
            "/flatblocks/",
            data=json.dumps(
                CreateFlatBlockSerializer(self.only_content_block).data
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)

        block = FlatBlock.objects.get(slug=self.only_content_block.slug)

        self.assertFalse(block.show_header, False)
        self.assertTrue(block.show_content, True)
        self.assertFalse(block.show_url, False)
        self.assertFalse(block.show_file, False)

    def test_only_url(self):
        response = self.client.post(
            "/flatblocks/",
            data=json.dumps(
                CreateFlatBlockSerializer(self.only_url_block).data
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)

        block = FlatBlock.objects.get(slug=self.only_url_block.slug)

        self.assertFalse(block.show_header)
        self.assertFalse(block.show_content)
        self.assertTrue(block.show_url)
        self.assertFalse(block.show_file)

    @skip("File validation error")
    def test_only_file(self):
        response = self.client.post(
            "/flatblocks/",
            data=json.dumps(
                CreateFlatBlockSerializer(self.only_file_block).data
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

        block = FlatBlock.objects.get(slug=self.only_file_block.slug)

        self.assertFalse(block.show_header)
        self.assertFalse(block.show_content)
        self.assertFalse(block.show_url)
        self.assertTrue(block.show_file)

    def test_header_content(self):
        response = self.client.post(
            "/flatblocks/",
            data=json.dumps(
                CreateFlatBlockSerializer(self.only_header_content_block).data
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

        block = FlatBlock.objects.get(slug=self.only_header_content_block.slug)

        self.assertTrue(block.show_header)
        self.assertTrue(block.show_content)
        self.assertFalse(block.show_url)
        self.assertFalse(block.show_file)

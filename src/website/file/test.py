from django.test import TestCase
from tastypie.test import ResourceTestCase
from .models import *
from .resource import *
from django.core.files.uploadedfile import SimpleUploadedFile


class FileTestCase(TestCase):
    def setUp(self):
        File.objects.create(title='test',
                            file=SimpleUploadedFile('best_file_eva.txt', 'these are the file contents!'),
                            type='text')

    def test_check_files_exists(self):
        self.assertIsNotNone(File.objects.all())

    def test_get_files_file(self):
        fl = File.objects.all()[0]
        self.assertIsNotNone(fl.file)

    def test_get_files_url(self):
        fl = File.objects.all()[0]
        self.assertIsNotNone(fl.file.url)
        self.assertEqual(fl.file.url, fl.get_url())


class FileResourceTestCase(ResourceTestCase):
    fixtures = ['test_file.json']

    def setUp(self):
        super(FileResourceTestCase, self).setUp()
        self.file_1 = File.objects.create(title='test',
                                          file=SimpleUploadedFile('best_file_eva.txt', 'these are the file contents!'),
                                          type='text')

        self.detail_url = '/api/v1/files/{0}/'.format(self.file_1.pk)

    def test_get_list_xml(self):
        self.assertValidXMLResponse(self.api_client.get('/api/v1/files/', format='xml'))

    def test_get_list_json(self):
        self.assertValidJSONResponse(self.api_client.get('/api/v1/files/', format='json'))

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url, format='json')
        self.assertValidJSONResponse(resp)
        self.assertKeys(self.deserialize(resp), ['title', 'file', 'type', 'id','created','modified','resource_uri','slug','url'])
        self.assertEqual(self.deserialize(resp)['title'], 'test')

    def test_get_detail_xml(self):
        self.assertValidXMLResponse(self.api_client.get(self.detail_url, format='xml'))

    def test_get_detail_json_url(self):
        resp = self.api_client.get(self.detail_url, format='json')
        self.assertValidJSONResponse(resp)

        self.assertEqual(self.deserialize(resp)['url'], self.file_1.get_url())

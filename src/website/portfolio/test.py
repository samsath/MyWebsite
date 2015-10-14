from django.test import TestCase
from tastypie.test import ResourceTestCase
from .models import *
from ..file.models import File
from .resource import *
from django.core.files.uploadedfile import SimpleUploadedFile


class LinkTestCase(TestCase):
    def setUp(self):
        self.fl = File.objects.create(title='test',
                                      file=SimpleUploadedFile('best_file_eva.txt', 'these are the file contents!'),
                                      type='text')
        Links.objects.create(title='tester file', file=self.fl)
        Links.objects.create(title='tester link', url='http://www.bbc.co.uk')
        Links.objects.create(title='tester both', file=self.fl, url='http://www.bbc.co.uk')

    def test_created_links(self):
        self.assertIsNotNone(Links.objects.all())

    def test_link_type_url(self):
        lk = Links.objects.get(title='tester link')
        self.assertEqual(lk.get_type(), 'url')

    def test_link_type_url_not_file(self):
        lk = Links.objects.get(title='tester link')
        self.assertNotEqual(lk.get_type(), self.fl.type)

    def test_link_type_file(self):
        lk = Links.objects.get(title='tester file')
        self.assertEqual(lk.get_type(), self.fl.type)

    def test_link_type_file_not_url(self):
        lk = Links.objects.get(title='tester file')
        self.assertNotEqual(lk.get_type(), 'url')

    def test_link_type_both(self):
        lk = Links.objects.get(title='tester both')
        self.assertEqual(lk.get_type(), 'both')

    def test_link_type_both_not_url(self):
        lk = Links.objects.get(title='tester both')
        self.assertNotEqual(lk.get_type(), 'url')

    def test_link_type_both_not_file(self):
        lk = Links.objects.get(title='tester both')
        self.assertNotEqual(lk.get_type(), self.fl.type)


class LinksResourceTestCase(ResourceTestCase):
    fixtures = ['test_link.json']

    def setUp(self):
        super(LinksResourceTestCase, self).setUp()
        self.fl = File.objects.create(title='test',
                                      file=SimpleUploadedFile('best_file_eva.txt', 'these are the file contents!'),
                                      type='text')
        self.link_1 = Links.objects.create(title='tester file', file=self.fl)
        self.link_2 = Links.objects.create(title='tester link', url='http://www.bbc.co.uk')
        self.link_3 = Links.objects.create(title='tester both', file=self.fl, url='http://www.bbc.co.uk')

        self.detail_url_1 = '/api/v1/links/{0}'.format(self.link_1.pk)
        self.detail_url_2 = '/api/v1/links/{0}'.format(self.link_2.pk)
        self.detail_url_3 = '/api/v1/links/{0}'.format(self.link_3.pk)

    def test_get_list_xml(self):
        self.assertValidXMLResponse(self.api_client.get('/api/v1/links/', format='xml'))

    def test_get_list_json(self):
        self.assertValidJSONResponse(self.api_client.get('/api/v1/links/', format='json'))

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url_1, format='json')
        self.assertValidJSONResponse(resp)
        self.assertKeys(self.deserialize(resp), ['title', 'file', 'id','created','modified','resource_uri','slug','url', 'background','foreground'])
        self.assertEqual(self.deserialize(resp)['title'], 'tester file')


class WorkTest(TestCase):
    def setUp(self):
        self.fl = File.objects.create(title='test',
                                      file=SimpleUploadedFile('best_file_eva.txt', 'these are the file contents!'),
                                      type='text')
        self.fl_two = File.objects.create(title='test two',
                                      file=SimpleUploadedFile('best_file_eva_two.txt', 'these are the file contents! two'),
                                      type='text')
        self.lk = Links.objects.create(title='tester link', url='http://www.bbc.co.uk')
        wone = Work(title='my idea', headline='hihih',description='None',is_public=True )
        wone.save()
        wone.links.add(self.lk)
        wone.content.add(self.fl)
        wteo = Work.objects.create(title='my idea two', headline='hihih', description='None', is_public=False )
        wteo.save()
        wteo.content.add(self.fl_two)

    def test_created_work(self):
        self.assertIsNotNone(Work.objects.all())


class WorkResourceTest(ResourceTestCase):
    fixtures = ['test_work.json']

    def setUp(self):
        super(WorkResourceTest, self).setUp()
        self.fl = File.objects.create(title='test',
                                      file=SimpleUploadedFile('best_file_eva.txt', 'these are the file contents!'),
                                      type='text')
        self.fl_two = File.objects.create(title='test two',
                                          file=SimpleUploadedFile('best_file_eva_two.txt', 'these are the file contents! two'),
                                          type='text')
        self.lk = Links.objects.create(title='tester link', url='http://www.bbc.co.uk')
        self.wone = Work(title='my idea', headline='hihih', description='None',is_public=True )
        self.wone.save()
        self.wone.links.add(self.lk)
        self.wone.content.add(self.fl)
        self.wteo = Work.objects.create(title='my idea two', headline='hihih', description='None', is_public=False )
        self.wteo.save()
        self.wteo.content.add(self.fl_two)

        self.detail_url_1 = '/api/v1/work/{0}'.format(self.wone.pk)
        self.detail_url_2 = '/api/v1/work/{0}'.format(self.wteo.pk)

    def test_get_list_xml(self):
        self.assertValidXMLResponse(self.api_client.get('/api/v1/work/', format='xml'))

    def test_get_list_json(self):
        self.assertValidJSONResponse(self.api_client.get('/api/v1/work/', format='json'))

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url_1, format='json')
        self.assertValidJSONResponse(resp)
        self.assertKeys(self.deserialize(resp), ['title', 'created', 'id', 'resource_uri', 'modified', 'slug', 'content', 'cover', 'themes', 'links', 'related', 'headline', 'description', 'date', 'is_public', 'background'])
        self.assertEqual(self.deserialize(resp)['title'], 'my idea')

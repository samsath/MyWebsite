from django.test import TestCase
from tastypie.test import ResourceTestCase
from .models import *
from .resource import *


class ThemesTestCase(TestCase):
    def setUp(self):
        Themes.objects.create(title='tester', sort_value=1, is_public=True)

    def test_get_created_theme(self):
        self.assertIsNotNone(Themes.objects.all())

    def test_get_theme_slug(self):
        theme = Themes.objects.get(id=1)
        self.assertEqual(theme.slug, 'tester')


class ThemesResourceTestCase(ResourceTestCase):

    fixtures = ['test_themes.json']

    def setUp(self):
        super(ThemesResourceTestCase, self).setUp()
        self.theme_1 = Themes.objects.create(title='tester', sort_value=1, is_public=True)
        self.detail_url = '/api/v1/themes/{0}/'.format(self.theme_1.pk)

    def test_get_list_xml(self):
        self.assertValidXMLResponse(self.api_client.get('/api/v1/themes/', format='xml'))

    def test_get_list_json(self):
        self.assertValidJSONResponse(self.api_client.get('/api/v1/themes/', format='json'))

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url, format='json')
        self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
        self.assertKeys(self.deserialize(resp), ['created', 'slug', 'title', 'id','is_public','modified','resource_uri','sort_value'])
        self.assertEqual(self.deserialize(resp)['title'], 'tester')

    def test_get_detail_xml(self):
        self.assertValidXMLResponse(self.api_client.get(self.detail_url, format='xml'))

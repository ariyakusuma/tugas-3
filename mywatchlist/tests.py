from django.test import SimpleTestCase
from mywatchlist.views import show_watchlist, show_xml, show_json
from django.urls import reverse, resolve

class TestUrls(SimpleTestCase):
    def test_show_mywatchlist_url(self):
        url = reverse('mywatchlist:show_watchlist')
        self.assertEqual(resolve(url).func, show_watchlist)

    def test_show_mywatchlistxml_url(self):
        url = reverse('mywatchlist:show_xml')
        self.assertEqual(resolve(url).func, show_xml)

    def test_show_mywatchlistjson_url(self):
        url = reverse('mywatchlist:show_json')
        self.assertEqual(resolve(url).func, show_json)


# Create your tests here.

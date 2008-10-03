import unittest
import datetime
import sys

from wsgi_intercept.urllib2_intercept import install_opener
import wsgi_intercept
from wsgi_test_app import create_wsgi_app

install_opener()
wsgi_intercept.add_wsgi_intercept('ws.audioscrobbler.com', 80, create_wsgi_app)
    
sys.path.append("..")
from src import Api

class TestTag(unittest.TestCase):
    """ A test class for the Album module. """
    
    def setUp(self):
        apikey = "152a230561e72192b8b0f3e42362c6ff"        
        self.api = Api(apikey, no_cache = True)#, debug = True)
        self.tag = self.api.getTag("rock").mostSimilar
        
    def tearDown(self):
        pass
        
    def testTagName(self):
        self.assertEqual(self.tag.name, "alternative")

    def testTagUrl(self):
        self.assertEqual(self.tag.url, "http://www.last.fm/tag/alternative")
    
    def testTagStreamable(self):
        self.assertEqual(self.tag.streamable, True)
        
    def testTagSimilar(self):
        tags = ['rock',
                'indie',
                'indie rock',
                'alternative rock',
                'seen live',
                'nasty pop',
                'electronic',
                'electronica',
                'kiwi indie niceness',
                'singer-songwriter'
                ]
        self.assertEqual([t.name for t in self.tag.similar[:10]], tags)
        
    def testTagMostSimilar(self):
        self.assertEqual(self.tag.mostSimilar.name, 'rock')
#        
#    def testAlbumReleaseDate(self):
#        date = datetime.datetime(1994, 7, 28, 0, 0)
#        self.assertEqual(self.album.releaseDate, date)
#        
#    def testAlbumImage(self):
#        self.assertEqual(self.album.image['small'], "http://userserve-ak.last.fm/serve/34/11846565.jpg")
#        self.assertEqual(self.album.image['medium'], "http://userserve-ak.last.fm/serve/64/11846565.jpg")
#        self.assertEqual(self.album.image['large'], "http://userserve-ak.last.fm/serve/174s/11846565.jpg")
#        self.assertEqual(self.album.image['extralarge'], "http://userserve-ak.last.fm/serve/300x300/11846565.jpg")
#    
#    def testAlbumStats(self):
#        self.assertEqual(self.album.stats.listeners, 14286)
#        self.assertEqual(self.album.stats.playcount, 39594)
#    
#    def testAlbumTopTags(self):
#        pass
#    
#    def testAlbumTopTag(self):
#        pass
#    
#    def testAlbumPlaylist(self):
#        self.assertEqual(self.album.playlist.url, "lastfm://playlist/album/2038492")        
    
if __name__ == '__main__':
    unittest.main()
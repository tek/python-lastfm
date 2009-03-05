#!/usr/bin/env python

__author__ = "Abhinav Sarkar <abhinav@abhinavsarkar.net>"
__version__ = "0.2"
__license__ = "GNU Lesser General Public License"

from lastfm.base import LastfmBase
from lastfm.mixins import Cacheable

class Shout(LastfmBase, Cacheable):
    """A class representing a shout."""

    def init(self,
             body = None,
             author = None,
             date = None):
        self._body = body
        self._author = author
        self._date = date
    
    @LastfmBase.cached_property
    def body(self):
        return self._body

    @LastfmBase.cached_property
    def author(self):
        return self._author

    @LastfmBase.cached_property
    def date(self):
        return self._date
    
    @staticmethod
    def _hash_func(*args, **kwds):
        try:
            return hash("%s%s" % (kwds['body'], kwds['author']))
        except KeyError:
            raise InvalidParametersError("body and author have to be provided for hashing")

    def __hash__(self):
        return self.__class__._hash_func(body = self.body, author = self.author)

    def __eq__(self, other):
        return (
                self.body == other.body and
                self.author == other.author
            )

    def __lt__(self, other):
        if self.author != other.author:
            return self.author < other.author
        else:
            if self.date != other.date:
                return self.date < other.date
            else:
                return self.body < other.body

    def __repr__(self):
        return "<lastfm.Shout: '%s' by %s>" % (self.body, self.author.name)
    
from lastfm.error import InvalidParametersError
    
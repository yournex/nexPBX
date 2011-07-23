"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_plugins(self):
        """Test Plugin system in Protocols"""
        import Protocols.plugins as p
        self.assertEqual(p.getPlugins()['SIP']['installed'], True )
        self.assertEqual(p.getPlugins()['SIP']['installed'], True )

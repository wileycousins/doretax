"""
Tests for the biz app.
"""

from django.utils import unittest
from biz.models import Association, AssocPosition

class AssociationTestCase(unittest.TestCase):
    def setUp(self):
        self.pencilSharperner = Association.objects.create(name="Nation Society of Pencil Sharpeners", type="civic")
        self.chamberOfCommerce = Association.objects.create(name="Chamber of Commerce", type="prof")
        self.chamberOfCommerce = Association.objects.create(name="Professional Tax People", type="prof", link="www.example.org")

#    def testRequired(self):
#        self.assertEqual(self.lion.speak(), 'The lion says "roar"')
#        self.assertEqual(self.cat.speak(), 'The cat says "meow"')

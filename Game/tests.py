from django.test import TestCase
from models import Update


class TestUpdate(TestCase):
	def setUp(self):
		update = Update()
		update.title = 'Test Update'
		update.season = 'Test Season'
		update.body = '**This should be bold**'
		update.save()

		self.update = update


	def test_to_html(self):
		expected = '<p><strong>This should be bold</strong></p>\n'
		actual = self.update.body_to_html()
		self.assertEqual(actual, expected)
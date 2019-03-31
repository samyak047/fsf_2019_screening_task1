
from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class IndexViewTests(TestCase):
	def test_default_index(self):
		'''
			test whether default home page is rendered or not
		'''
		response = self.client.get(reverse('home'))
		self.assertEquals(response.status_code,200)
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class Snacks_Test(SimpleTestCase):
    def test_home_page_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'home.html')

    def test_about_page_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'about.html')
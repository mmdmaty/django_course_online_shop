from django.test import TestCase
from django.urls import reverse


class TestPages(TestCase):
    def test_home_page_status_code_with_path(self):
        response = self.client.get('')
        self.assertEqual(first=response.status_code, second=200)

    def test_home_page_status_code_with_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(first=response.status_code, second=200)

    def test_home_page_templates(self):
        response = self.client.get('')
        self.assertTemplateUsed(
            response=response, template_name='pages_home.html')
    
    def test_home_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response=response,text='home page')

    def test_about_us_statuscode_by_path(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(first=response.status_code,second=200)

    def test_about_us_statuscode_by_name(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(first=response.status_code,second=200)
    
    def test_about_us_content(self):
        response = self.client.get(reverse('aboutus'))
        self.assertContains(response=response,text='about us page')
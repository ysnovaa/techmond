from django.test import TestCase, Client
from .models import Product
from django.urls import reverse
from django.http import HttpRequest

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name='Example Product', price=100, description='This is an example product description.')

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_description_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_name_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 40)

    def test_price_is_positive(self):
        product = Product.objects.get(id=1)
        self.assertTrue(product.price >= 0)

    def test_str_method(self):
        product = Product.objects.get(id=1)
        expected_object_name = product.name
        self.assertEquals(expected_object_name, str(product))




class HomeViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')

    def test_home_view_with_no_product_ids(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecom/index.html')
        self.assertNotContains(response, 'afterlogin')
        self.assertEqual(response.context['product_count_in_cart'], 0)

    def test_home_view_with_product_ids(self):
        request = HttpRequest()
        request.COOKIES['product_ids'] = '1|2|3'
        response = self.client.get(self.home_url, request=request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecom/index.html')
        self.assertNotContains(response, 'afterlogin')
        self.assertEqual(response.context['product_count_in_cart'], 3)

    def test_home_view_authenticated_user(self):
        self.client.login(username='failuser', password='12345') 
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, 'afterlogin')

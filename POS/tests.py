from django.test import TestCase
from home.models import Order
# Create your tests here.
class PosTests(TestCase):
    def setUp(self):
        Order.objects.create(
            table='A23',
            custumer = 'test',
        )
    def test_string_representation(self):
        order = Order(table="A23")
        self.assertAlmostEqual(str(order), order.table)
    def test_post_list_view(self):
        response = self.client.get('/POS/')
        self.assertAlmostEqual(response.status_code, 200)
        self.assertContains(response, 'A23')
        self.assertTemplateUsed(response, 'html/pos.html')
    def test_post_detail_view(self):
        response = self.client.get('/POS/1')
        self.assertAlmostEqual(response.status_code, 200)
        self.assertContains(response, 'A23')
        self.assertTemplateUsed(response, 'html/pos_id.html')
    



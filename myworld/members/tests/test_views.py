from django.test import TestCase, Client
from django.urls import reverse
from members.models import *
import json
from datetime import datetime
from members.views import CTM

class TestViews(TestCase):
    def setUp(self):
        # global CTM
        # CTM = RegistetUser.objects.create(username='a',password='1',email='12@gmail.com')
        # self.C1 = Customer.objects.create(idctm=CTM,namectm='a',address_field='a',phone='1',Avatar='a')
        # # self.product = Product.objects.create(idpd='P1')

        self.client = Client()
        self.home_url = reverse('home')
        self.cart_url = reverse('cart')
        self.deleteCart_url = reverse('deleteCart', args=['P1'])
        self.service_url = reverse('service')
        self.signup_url = reverse('signup')
        self.signin_url = reverse('signin')
        self.viewAllPd_url = reverse('viewAllPd', args=['CLOTHES'])
        self.viewPd_url = reverse('viewPd', args=['P1'])
        self.logout_url = reverse('logout')
        self.enterProfile_url = reverse('enterProfile')
        self.viewProfile_url = reverse('viewProfile')
        self.payment_url = reverse('payment')


    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_cart_GET(self):
        response = self.client.get(self.cart_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

    def test_service_GET(self):
        response = self.client.get(self.service_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'service.html')

    def test_signup_GET(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signin_GET(self):
        response = self.client.get(self.signin_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')

    def test_viewAllPd_GET(self):
        response = self.client.get(self.viewAllPd_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ViewAllPd.html')

    def test_logout_GET(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 302)
        # self.assertEquals(response, self.home_url)

    def test_enterProfile_GET(self):
        response = self.client.get(self.enterProfile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'EnterProfile.html')

    # def test_viewProfile_GET(self):
    #     response = self.client.get(self.viewProfile_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'ViewProfile.html')

    # def test_payment_GET(self):
    #     response = self.client.get(self.payment_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'Payment.html')

    # def test_viewPd_GET(self):
    #     response = self.client.get(self.viewPd_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'ViewPd.html')

    # def test_deleteCart_GET(self):
    #     global CTM
    #     CTM = RegistetUser.objects.create(username='a',password='1',email='12@gmail.com')
    #     self.C1 = Customer.objects.create(idctm=CTM,namectm='a',address_field='a',phone='1',Avatar='a')
        
    #     response = self.client.get(self.deleteCart_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'cart.html')

    # def test_service_POST(self):
    #     response = self.client.post(self.service_url, {
    #         'TypeSv':'SV1',
    #         'Date': datetime.strptime('2023-1-1',"%Y-%m-%d")
    #     })
    #     self.assertEquals(response.status_code, 302)
    #     # self.assertEquals(response., 'service.html')

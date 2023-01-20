from django.test import SimpleTestCase
from django.urls import reverse, resolve
from members.views import *

class TestUrls(SimpleTestCase):
    def test_home_url_is_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_cart_url_is_resolves(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func, cart)

    def test_deleteCart_url_is_resolves(self):
        url = reverse('deleteCart', args=['P1'])
        self.assertEquals(resolve(url).func, deleteCart)

    def test_service_url_is_resolves(self):
        url = reverse('service')
        self.assertEquals(resolve(url).func, service)

    def test_signup_url_is_resolves(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

    def test_signin_url_is_resolves(self):
        url = reverse('signin')
        self.assertEquals(resolve(url).func, signin)

    def test_ViewAllPd_url_is_resolves(self):
        url = reverse('viewAllPd', args=['CLOTHES'])
        self.assertEquals(resolve(url).func, ViewAllPd)

    def test_ViewPd_url_is_resolves(self):
        url = reverse('viewPd', args=['P1'])
        self.assertEquals(resolve(url).func, ViewPd)

    def test_Logout_url_is_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, Logoutpage)

    def test_enterProfile_url_is_resolves(self):
        url = reverse('enterProfile')
        self.assertEquals(resolve(url).func, EnterProfile)

    def test_ViewProfile_url_is_resolves(self):
        url = reverse('viewProfile')
        self.assertEquals(resolve(url).func, ViewProfile)

    def test_Payment_url_is_resolves(self):
        url = reverse('payment')
        self.assertEquals(resolve(url).func, Payment)
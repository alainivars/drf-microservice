import unittest

from rest_framework import status
from rest_framework.reverse import reverse

from my_api.rest.tests.base import BaseTestCase


class BasicTestCase(BaseTestCase):

    def test_api_handler400(self):
        response = self.client.get(reverse('handler400'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_handler403(self):
        response = self.client.get(reverse('handler403'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_handler404(self):
        response = self.client.get(reverse('handler404'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_handler500(self):
        response = self.client.get(reverse('handler500'))
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_authorization_is_enforced(self):
        response = self.client.get(reverse('icinga'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_with_false_credential(self):
        response = self.basics_auth_get(
            reverse('icinga'),
            username="admin",
            password="admin"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_with_false_token(self):
        false_token = "c2dffbda4f73937afb13ce8dc281759a8b"
        response = self.token_auth_get(
            reverse('icinga'),
            false_token
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


if __name__ == '__main__':
    unittest.main()

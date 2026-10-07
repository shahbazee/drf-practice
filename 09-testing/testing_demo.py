from rest_framework import status
from rest_framework.test import APITestCase


class BookAPITest(APITestCase):
    def test_list_books(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_case_book_authorized(self):
        data = {"title": "Test", "author": "Ali",
                "price": "100.00", "published": "2026-01-01"}
        response = self.client.post("/book/", data)
        self.assertEqual(response.status_code, 
                         status.HTTP_401_UNAUTHORIZED)
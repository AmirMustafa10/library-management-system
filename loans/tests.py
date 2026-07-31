from django.test import TestCase


class MyLoansPageTests(TestCase):
    def test_my_loans_page_loads_placeholder_layout(self):
        response = self.client.get("/loans/my/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, "My Loans")
        self.assertContains(response, "Placeholder")

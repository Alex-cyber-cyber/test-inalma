
import json
from django.urls import reverse
from rest_framework.test import APITestCase
from src.catalog.models import Product

class ProductAPITests(APITestCase):
    fixtures = ["src/catalog/fixtures/products.json"]

    def test_list_basic(self):
        url = reverse("product-list-create")
        res = self.client.get(url)
        assert res.status_code == 200
        data = res.json()
        assert "results" in data
        assert data["count"] >= 5

    def test_search_and_filter(self):
        url = reverse("product-list-create")
        res = self.client.get(url, {"q": "mo"})
        names = [p["name"].lower() for p in res.json()["results"]]
        assert any("monitor" in n for n in names)

        res = self.client.get(url, {"min_price": "200", "max_price": "300"})
        prices = [float(p["price"]) for p in res.json()["results"]]
        assert all(200 <= p <= 300 for p in prices)

    def test_tags_and_ordering(self):
        url = reverse("product-list-create")
        res = self.client.get(url, {"tags": "tech,pc", "ordering": "-price"})
        results = res.json()["results"]
        assert all("tech" in [t.lower() for t in r["tags"]] for r in results)
        assert results == sorted(results, key=lambda r: r["price"], reverse=True)

    def test_create_unique_case_insensitive(self):
        url = reverse("product-list-create")
        payload = {"name": "monitor", "price": "399.00", "tags": ["pc"]}
        res = self.client.post(url, data=json.dumps(payload), content_type="application/json")
        assert res.status_code == 400
        assert "insensible" in json.dumps(res.json()).lower()

        payload2 = {"name": "New Product", "price": "10.00", "tags": []}
        res2 = self.client.post(url, data=json.dumps(payload2), content_type="application/json")
        assert res2.status_code == 201
        assert Product.objects.filter(name__iexact="new product").exists()

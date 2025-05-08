from django.test import TestCase
from django.contrib.auth.models import User
from mizan_recommendation.models import Product, Transaction
from mizan_recommendation.recommendation_engine import generate_recommendations

class RecommendationEngineTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.product1 = Product.objects.create(name="Laptop",price=1200.00)
        self.product2 = Product.objects.create(name="Phone", price=550.00)
        self.product3 = Product.objects.create(name="Headphones", price=320.00)

        # User buys one product
        Transaction.objects.create(user=self.user, product=self.product1, amount=1200.00)

    def test_generate_recommendations(self):
        recommendations = generate_recommendations(self.user)
        recommended_product_names = [p.name for p in recommendations]

        self.assertNotIn("Laptop", recommended_product_names)  # Should not recommend what user bought
        self.assertIn("Phone", recommended_product_names)  # Other products should be recommended
        self.assertIn("Headphones", recommended_product_names)



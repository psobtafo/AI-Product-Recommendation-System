from django.shortcuts import render

# Create your views here.
# views.py (in your recommendations app)

from django.shortcuts import render
from django.http import JsonResponse
from .models import Transaction, Product
from .recommendation_engine import generate_recommendations

def user_recommendations(request, user_id):
    # Get the user's transaction history
    transactions = Transaction.objects.filter(user_id=user_id)
    product_ids = [transaction.product.id for transaction in transactions]

    # Get recommendations based on the user's past purchases
    recommended_products = generate_recommendations(product_ids)

    # Return the top recommended products in the response
    products = Product.objects.filter(id__in=recommended_products)
    response_data = [{'name': product.name, 'category': product.category, 'price': str(product.price)} for product in products]

    return JsonResponse({'recommendations': response_data})

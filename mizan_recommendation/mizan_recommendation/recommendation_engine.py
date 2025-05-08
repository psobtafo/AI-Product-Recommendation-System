# recommendation_engine.py (inside your recommendations app)

from mizan_recommendation.models import Product, Transaction

def generate_recommendations(purchased_product_ids):
    # Here you could implement your recommendation algorithm
    # For example, a basic collaborative filtering or content-based algorithm
    # For simplicity, this could just be a dummy function that recommends products
    # that are similar to those in the user's purchase history.

    # Get all purchased product IDs for the given user
    purchased_product_ids = Transaction.objects.filter(user=user).values_list('product_id', flat=True)
    
    # Debugging statements
    print(f"purchased_product_ids: {list(purchased_product_ids)}")
    print(f"Type of purchased_product_ids: {type(purchased_product_ids)}")

    # Fetch the purchased products
    purchased_products = Product.objects.filter(id__in=purchased_product_ids)
    
    recommended_ids = []  # List of recommended product IDs

    # Dummy example: Recommend products from the same category as purchased products
    #purchased_products = Product.objects.filter(id__in=purchased_product_ids)
    #purchased_product_ids = Transaction.objects.filter(user=user).values_list('product_id', flat=True)
    #Debuggin statements
    #print(f"purchased_product_ids: {purchased_product_ids}")  
    #print(f"Type of purchased_product_ids: {type(purchased_product_ids)}")

    for product in purchased_products:
        similar_products = Product.objects.filter(category=product.category).exclude(id__in=purchased_product_ids)
        recommended_ids.extend(similar_products.values_list('id', flat=True))

    return recommended_ids[:10]  # Return top 10 recommended products


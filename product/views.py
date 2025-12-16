from django.db.models import Count
from .models import Product, Category, Review
from django.db.models import Avg
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import CategorySerializer,ProductSerializer,ReviewSerializer, ProductWithReviewsSerializer

class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.annotate(product_count=Count("product"))
    serializer_class = CategorySerializer

class CategoryDetalView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.annotate(product_count=Count('product'))
    serializer_class = CategorySerializer
    lookup_field = "id"

class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



class ReviewDetalView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "id"

class ProductWithReviewsView(ListAPIView):
    queryset = Product.objects.annotate(
        rating=Avg("reviews__stars")
    )
    serializer_class = ProductWithReviewsSerializer

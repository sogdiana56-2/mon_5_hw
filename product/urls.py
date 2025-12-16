from django.urls import path
from . views import (
CategoryListCreateView,CategoryDetalView, ProductListCreateView,ProductDetailView, ReviewListCreateView, ReviewDetalView,ProductWithReviewsView, )

urlpatterns = [
    path("products/", ProductListCreateView.as_view()),
    path("products/<int:id>/", ProductDetailView.as_view()),
    path("categories/", CategoryListCreateView.as_view()),
    path("categories/<int:id>/",CategoryDetalView.as_view()),
    path("reviews/", ReviewListCreateView.as_view()),
    path("reviews/<int:id>/", ProductDetailView.as_view()),
]
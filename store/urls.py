from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    path('product/', views.ProductViewSet.as_view({'get': 'list'})),
    path('product/<int:pk>/', views.ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('product/create/', views.ProductViewSet.as_view({'post': 'create'})),

    path('author/', views.AuthorViewSet.as_view({'get': 'list'})),
    path('author/<int:pk>/', views.AuthorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('author/create/', views.AuthorViewSet.as_view({'post': 'create'})),

    path('publisher/', views.PublisherViewSet.as_view({'get': 'list'})),
    path('publisher/<int:pk>/', views.PublisherViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('publisher/create/', views.PublisherViewSet.as_view({'post': 'create'})),

    path('category/', views.CategoryViewSet.as_view({'get': 'list'})),
    path('category/<int:pk>/', views.CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('category/create/', views.CategoryViewSet.as_view({'post': 'create'})),

    path('contact/', views.ContactViewSet.as_view({'get': 'list'})),
    path('contact/<int:pk>/', views.ContactViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('contact/create/', views.ContactViewSet.as_view({'post': 'create'})),

    path('genre/', views.GenreViewSet.as_view({'get': 'list'})),
    path('genre/<int:pk>/', views.GenreViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('genre/create/', views.GenreViewSet.as_view({'post': 'create'})),

    path('review/', views.ReviewViewSet.as_view({'get': 'list'})),
    path('review/<int:pk>/', views.ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('review/create/', views.ReviewViewSet.as_view({'post': 'create'})),
])

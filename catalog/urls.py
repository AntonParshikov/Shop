from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import CategoryListView, ProductListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductDetailView, CategoryProductDetailView, in_stock
from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path('category/<int:pk>/', CategoryListView.as_view(), name='category_list'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/', cache_page(60)(ProductListView.as_view()),  name='product_list'),
    path('<int:pk>/product/', cache_page(60)(CategoryProductDetailView.as_view()), name='category_product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_confirm_delete'),
    path('stock/<int:pk>/', in_stock, name='in_stock'),
    path('contacts/', views.contacts, name='contacts'),

]

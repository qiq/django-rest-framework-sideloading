from rest_framework import viewsets

from drf_sideloading.mixins import SideloadableRelationsMixin
from tests.models import (
    Product,
    Category,
    Supplier,
    Partner)

from tests.serializers import ProductSerializer, CategorySerializer, SupplierSerializer, PartnerSerializer


class ProductViewSet(SideloadableRelationsMixin, viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    base_model_name = 'product'

    sideloadable_relations = {
        'product': ProductSerializer,
        'category': CategorySerializer,
        'supplier': SupplierSerializer,
        'partner': PartnerSerializer
    }


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer



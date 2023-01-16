from .models import Product, Brand
from rest_framework import viewsets
from .serializers import ProductSerializer, BrandSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = []

class BrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow brands to be viewed or edited
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = []

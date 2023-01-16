from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Brand
from .serializers import ProductSerializer, BrandSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class BrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow brands to be viewed or edited
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
def product_list(request):
    """
    List all the products for non protected views
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def product_view(request,id):
    """
    List all the products for non protected views
    """
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        # Increment the number ov views
        product.count +=1
        product.save()
        return Response(serializer.data)

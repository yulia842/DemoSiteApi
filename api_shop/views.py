from rest_framework import viewsets
from .models import Product, Cart
from .serializers import ProductSerializer, CartSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )

    @action(methods=['POST'], detail=True)
    def add_to_cart(self, request,pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        product = Product.objects.get(id=pk)
        user = request.user
        quantity = int(request.data.get('quantity', 1))

        cart_item, created = Cart.objects.get_or_create(user=user, product=product, defaults={'quantity': quantity})
        if not created :
            cart_item.quantity += quantity
            cart_item.save()
        serializer = CartSerializer(cart_item, many=False)
        return Response({"detail": "Product added to cart", 'data' : serializer.data}, status=status.HTTP_200_OK)
    
    
    @action(methods=['POST'], detail=False)
    def add_product(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"detail": "Product added to cart", 'data' : serializer.data}, status=status.HTTP_201_CREATED)
        
    
    


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
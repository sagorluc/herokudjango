from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from Product_app.models import Product

# Create your views here.

@api_view(['GET', 'POST'])
def product_view(request):
    
    if request.method == 'GET':
        id = request.data.get('id')
        
        if id is not None:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        
        products = Product.objects.all().filter(is_available=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
       json_data = request.data, request.data['file']
       serializer = ProductSerializer(data=json_data)
       if serializer.is_valid():
           serializer.save()
           res = {'message': 'data inserted'}
           return Response(res, status=status.HTTP_201_CREATED) 
       else:
           res_err = serializer.errors
           return Response(res_err, status=status.HTTP_400_BAD_REQUEST)
    
        

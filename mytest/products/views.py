from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from products.serializers import UserSerializer, GroupSerializer
from products.models import Products, UserModel
from products.serializers import ProductSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer



# @api_view(['GET', 'POST'])
# def product_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         products = Products.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         product = Products.objects.get(pk=pk)
#     except Products.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

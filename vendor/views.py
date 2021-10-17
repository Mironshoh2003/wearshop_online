from requests import Response
from rest_framework import viewsets, generics
from rest_framework import permissions
from vendor.models import Food, Category
from vendor.serializers import FoodSerializer, CategorySerializer


class FoodGeneric(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodGenericCreateView(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryGeneric(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryGenericCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

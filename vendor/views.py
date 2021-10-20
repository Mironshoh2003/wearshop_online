from requests import Response
from rest_framework import viewsets, generics
from rest_framework import permissions
from vendor.models import Food, Category
from vendor.serializers import FoodSerializer, CategorySerializer


class FoodGeneric(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodGenericCategoryView(generics.ListAPIView):
    serializer_class = FoodSerializer

    def get_queryset(self,pk):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        return Food.objects.filter(category__id=pk)


class CategoryGeneric(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryGenericCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

from django.urls import path

from vendor.views import FoodGeneric, FoodGenericCategoryView, CategoryGeneric, CategoryGenericCreateView

app_name = "vendor"
urlpatterns = [
    path('food/', FoodGeneric.as_view(), name='food'),
    path('food/<int:pk>', FoodGenericCategoryView.as_view(), name='food-create'),
    path('category/', CategoryGeneric.as_view(), name='category'),
    path('category/create', CategoryGenericCreateView.as_view(), name='category-create')
]

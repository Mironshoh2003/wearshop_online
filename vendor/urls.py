from django.urls import path

from vendor.views import FoodGeneric,FoodGenericCreateView

app_name = "vendor"
urlpatterns = [
    path('food/', FoodGeneric.as_view(), name='food'),
    path('food/create', FoodGenericCreateView.as_view(), name='food-create'),

]

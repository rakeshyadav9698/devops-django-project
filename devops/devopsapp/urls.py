from django.urls import path
from . import views

app_name = 'devopsapp'

urlpatterns = [
    path('items', views.GetProductList.as_view(), name='item-list'),
    path('add', views.AddProduct.as_view(), name='create'),
    path('delete', views.DeleteProduct.as_view(), name='delete'),
]
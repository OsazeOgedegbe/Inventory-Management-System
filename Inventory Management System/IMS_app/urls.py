from django.urls import path
from IMS_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory/', views.inventory, name='inventory'),
    path('orders/', views.orders, name='orders'),
    path('about/', views.about, name='about'),
    #path('order_view/', views.order_view, name='order_view'),
    path('item/<int:pk>/delete/', views.delete_item, name='delete_item'),
    path('item/<int:pk>/increment/', views.increment_item, name='increment_item'),
    path('item/<int:pk>/decrement/', views.decrement_item, name='decrement_item'),
    path('edit_item/<int:pk>/', views.edit_item, name='edit_item'),
    #path('order/<int:pk>/view/', views.view_order, name='view_order'),

]
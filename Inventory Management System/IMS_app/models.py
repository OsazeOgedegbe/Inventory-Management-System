from django.db import models

class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(primary_key=True)
    shipping_address = models.TextField(max_length=200)

    def __str__(self):
        return str(self.full_name)
    
    

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateField()
    shipping_address = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return str(self.order_id)



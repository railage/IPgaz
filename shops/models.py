from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='shops/', blank=True, null=True)
    latitude = models.FloatField(default=55.796)
    longitude = models.FloatField(default=49.106)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    shops = models.ManyToManyField(Shop, related_name='categories')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    delivery_schedule = models.CharField(max_length=100, blank=True)
    shops = models.ManyToManyField(Shop, related_name='products')

    def __str__(self):
        return self.name

class Order(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='orders')
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    product_request = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ от {self.customer_name} в {self.shop.name}"
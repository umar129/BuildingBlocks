from django.db import models

# Create your models here.
class Cust_acc(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    mobile = models.BigIntegerField(unique=True)
    email = models.EmailField(max_length=30)
    address = models.TextField(max_length=225)
    token = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Cust_store(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    mail = models.EmailField(max_length=30,default='store@gmail.com')
    number = models.BigIntegerField()
    address = models.TextField(max_length=255)
    cust_id = models.ForeignKey(Cust_acc,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.category


class Product_info(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    mrp = models.FloatField()
    sele_price = models.FloatField()
    image = models.FileField(upload_to='products/')
    discription = models.TextField()
    store_id = models.ForeignKey(Cust_store,on_delete=models.CASCADE)
    cust_id = models.ForeignKey(Cust_acc,on_delete=models.CASCADE)

    def __str__(self):
        return self.id,self.name,self.image

class Orders(models.Model):
    id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product_info,on_delete=models.CASCADE)
    store_id = models.ForeignKey(Cust_store,on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Cust_acc,on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)



from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=30000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")
    shop_id = models.ForeignKey("Shopdetail",default=101, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name


class Shopdetail(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    shop_name = models.CharField(max_length=50)
    shop_addr = models.CharField(max_length=500, default="")
    shop_city = models.CharField(max_length=100, default="")
    shop_state = models.CharField(max_length=50, default="")
    shop_zip_code = models.CharField(max_length=50, default="")
    # shop_mobilenumber = PhoneNumberField()
    shop_email = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.shop_name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=50, default="")
    zip_code = models.CharField(max_length=50, default="")
    # mobilenumber = PhoneNumberField()

    def __str__(self):
        return self.name






class orderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    # mobilenumber = PhoneNumberField()
    query = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.name




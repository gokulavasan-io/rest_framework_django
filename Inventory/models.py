from django.db import models

class Category(models.Model):
    category_name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.category_name
    
class Products(models.Model):
    category_reference=models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100,null=True)
    code=models.CharField(max_length=100,null=100)
    price=models.FloatField(default=0)
    
    def __str__(self):
        return self.product_name
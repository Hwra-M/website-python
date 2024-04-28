from django.db import models

# Create your models here.
#items on sale
class Destination(models.Model) :
    name= models.CharField(max_length =100)
    img=models.ImageField(upload_to='pics') 
    des=models.TextField()
    price=models.IntegerField() 

#products
class Products(models.Model) :
    name= models.CharField(max_length =100)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()
    offer=models.TextField(default='no offer') 
    price=models.IntegerField() 

#This class for storing the purchased products details 
class PProducts(models.Model) :
    pcname= models.CharField(max_length =100)
    pcadd1= models.CharField(max_length =100)
    pcmobile=models.TextField()
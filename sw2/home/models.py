from django.db import models
from django.shortcuts import reverse

# Create your models here.
class books(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.CharField(max_length=200,blank=True)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    borrow=models.IntegerField(null=True)


    def __str__(self):
        return self.name
    
    def get_image_url(self):
        return f'/media/{self.image}'

    def get_show_url(self):
        return reverse('book.show',args=[self.id])

    def get_delete_url(self):
        return reverse('book.delete',args=[self.id])    
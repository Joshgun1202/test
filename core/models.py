from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    img = models.ImageField(upload_to='img/')
    name = models.CharField(max_length=100)
    icon=models.CharField(max_length=50,default="fas fa-tv")

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name



class Item(models.Model):
    img = models.ImageField(upload_to='img/',blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    media = models.FileField(upload_to='files/')
    text = RichTextField()
    
    class Meta:
        db_table = 'item'
        verbose_name = 'item'
        verbose_name_plural = 'items'

    


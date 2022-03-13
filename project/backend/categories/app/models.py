from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, SlugField)



class Category(Model):
    name = CharField(max_length=128)
    slug = SlugField(max_length=256)
    img = ImageField(upload_to='project/%Y/%m/%d')


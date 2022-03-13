from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)



class Category(Model):
    name = CharField(max_length=128)
    project_img = ImageField(upload_to='project/%Y/%m/%d')
    project_url = TextField(blank=True, null=True)
    github_url = TextField()

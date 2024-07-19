from django.db import models
from django.db import models
from django.shortcuts import render


class Blogs(models.Model):
   title=models.CharField(max_length=255)
   content=models.TextField()

# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.





class Analise(models.Model):

    STATUS = (
        ('Submit','Submit'),
    )

    doenca = models.CharField(max_length=255, verbose_name ='Doença')
    done = models.CharField(
        max_length=1,
        choices=STATUS,
    )



    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now= True)







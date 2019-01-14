from django.db import models


class Billboard(models.Model):
    title = models.CharField(max_length=50, null=False)
    text = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=30, null=False)

    objects = models.Manager()

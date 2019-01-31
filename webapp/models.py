from django.db import models


class UserDetails(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class data(models.Model):
    user = models.CharField(max_length=20)
    movie = models.CharField(max_length=40)

    def __str__(self):
        return self.user
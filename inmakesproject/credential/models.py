# from django.db import models
# from django.urls import reverse
# from django.contrib.auth.models import User
#
#
# class User(models.Model):
#
#    username=models.CharField(max_length=250,unique=True)
#    first_name=models.CharField(max_length=250,unique=True)
#    last_name=models.CharField(max_length=250,unique=True)
#    email = models.EmailField(max_length=254, unique=True)
#    password = models.CharField(max_length=128)
#
#
#
#    def get_url(self):
#        return reverse('profile_detail', kwargs={'username': self.username})
#
#    def __str__(self):
#       return '{}'.format(self.username)
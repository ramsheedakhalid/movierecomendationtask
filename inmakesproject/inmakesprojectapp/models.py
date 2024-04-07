from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)


    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('inmakesprojectapp:movie_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Movie(models.Model):

    title=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    poster=models.ImageField(upload_to='movie',blank=True)
    releasedate=models.DateTimeField(auto_now_add=True)
    actors=models.TextField(blank=True)
    link = models.URLField(max_length=200)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        ordering=('title',)
        verbose_name='movie'
        verbose_name_plural='movies'

    def get_url(self):
        return reverse('inmakesprojectapp:movieCatdetail',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.title)



class Review(models.Model):
    title = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.title.movie}"





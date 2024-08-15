from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    content = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name = 'Article'
        ordering = ['-date']

    @property
    def publish_string(self):
        return 'L article a ete publie' if self.published else 'Pas encore publie'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #    return reverse('blog-detail', kwargs={'slug': self.slug})

    @property
    def world_count(self):
        return len(self.content.split())

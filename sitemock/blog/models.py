from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify

def create_slug(title):
    slug = slugify(title)
    qs = Post.objects.filter(slug__icontains=slug).order_by("id")
    exists = qs.exists()
    if exists:
        slug = "%s-%s" %(slug, (qs.count() + 1))
    return slug

class QueryPost(models.Manager):
    def search(self,query):
        return self.filter(models.Q(title__icontains=query) | models.Q(text__icontains=query))

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField('Criado em', default=timezone.now, auto_created=True)
    published_date = models.DateTimeField('Publicado em', blank=True, null=True, auto_created=True)
    updated_at = models.DateTimeField('Atualizado em', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        ordering = ['-published_date']

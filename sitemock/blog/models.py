from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify

def create_slug(title):
    slug = slugify(title)
    qs = Post.objects.filter(slug__icontains=slug)
    exists = qs.exists()
    if exists:
        slug = "%s-%s" %(slug, qs.last().id)
    return slug

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self.title)
        return super().save(*args, **kwargs)

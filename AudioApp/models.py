from django.db import models
from django.utils.text import slugify

class AudioFile(models.Model):
    title = models.CharField(max_length=100)
    audio = models.FileField(upload_to='audio/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
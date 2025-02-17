from django.db import models
from embed_video.fields import EmbedVideoField

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    video = EmbedVideoField(blank=True)  # Optional video
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

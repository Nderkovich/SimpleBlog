from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,
                            related_name="post",
                            on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_shared = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_created',)

    def get_absolute_url(self):
        return reverse('post:detail_detail', self.id)


from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=20)
    title = models.CharField(max_length=144)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '[{}] {}'.format(self.user_id, self.title)
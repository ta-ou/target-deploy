from django.db import models
from django.conf import settings

class Target(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    target = models.CharField(max_length=20)
    target_reason = models.CharField(max_length=20)
    target_term = models.CharField(max_length=20)
    small_target_1 = models.CharField(max_length=20)
    small_target_2 = models.CharField(max_length=20)
    small_target_3 = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="targets")
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="votes")
    done_comment = models.TextField(null=True)

    # def __str__(self):
    #     return self.target, self.target_reason, self.target_term, self.small_target_1, self.small_target_2, self.small_target_3
 
class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    target = models.ForeignKey(Target, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username

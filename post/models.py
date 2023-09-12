# user/models.py
from django.db import models
from user.models import UserModel


# Create your models here.
class PostModel(models.Model):
    class Meta:
        db_table = "my_post"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=20, null=False)
    contents = models.TextField(null=False)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, null=True)

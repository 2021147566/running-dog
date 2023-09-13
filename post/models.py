# user/models.py
from django.db import models
from user.models import UserModel


# Create your models here.
class PostModel(models.Model):
    class Meta:
        db_table = "my_post"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    place_name = models.TextField(null=False, blank=False)
    contents = models.TextField(null=False)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

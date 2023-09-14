from django.db import models


class UserModel(models.Model):
    class Meta:
        db_table = "my_user"

    name = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)
    email = models.CharField(max_length=256, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=200)
    userbio= models.TextField(max_length=200, null = True, blank = True)
    content=models.TextField()
    created_at=models.DateField(auto_now_add=True)

    class Meta:#Creates permissions for user
        permissions = [
            ("create", "Can Create Posts"),#Users with create permission can create posts
            ("read", "Can Read Posts"),#Read permission is for users to read posts
            ("edit", "Can Edit Posts"),#edit 
        ]
        # This is going to the UI
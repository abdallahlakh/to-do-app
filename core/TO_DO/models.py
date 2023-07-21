from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Mission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=10)
    description=models.TextField()
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
from django.db import models
from users.models import Users
# Create your models here.
class Tusk(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Users,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.title
from django.db import models

class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    content = models.TextField(max_length=400)
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

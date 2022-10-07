from django.db import models

# Create your models here.
class UserMessage(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=300)
    date_in = models.DateTimeField(auto_now_add=True)
  
    class Meta:
        verbose_name_plural = 'User messages'
        ordering = ('date_in', )

    def __str__(self):
         return f"{self.date_in} {self.name}, {self.email}, {self.subject}: {self.message}"
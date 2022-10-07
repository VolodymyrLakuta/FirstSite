from tokenize import blank_re
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class BookTable(models.Model):

    mobile_re = RegexValidator(regex=r"^(\d{3}-\d{3}-\d{4})$", message="Wrong phone number")

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, validators=[mobile_re])
    date = models.DateField()
    time = models.TimeField()
    people_numb = models.SmallIntegerField()
    message = models.TextField(max_length=300)

    date_in = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('date_in', )

    def __str__(self):
        visual = f"{self.date_in} {self.name}, phone {self.phone}, "
        visual += f"{self.date} {self.time} people {self.people_numb} msg: {self. message[:30]}"
        return visual
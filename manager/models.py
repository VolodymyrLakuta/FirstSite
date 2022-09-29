from xml.etree.ElementInclude import default_loader
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class BookTable(models.Model):

    mobile_re = RegexValidator(regex=r"^(\d{10})$", message="Wrong phone number")

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, validators=[mobile_re])
    date = models.DateField()
    time = models.TimeField()
    people_numb = models.SmallIntegerField()
    message = models.TextField(max_length=300)

    is_processed = models.BooleanField(default=False)
    date_in = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_in', )

    def __str__(self):
        visual = f"/n{self.date_in} {self.name}, phone {self.phone}"
        visual += f"/norder: {self.date} {self.time} people {self.people_numb} /n{self. message[:30]}"
        return visual
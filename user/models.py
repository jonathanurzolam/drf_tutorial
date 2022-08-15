import email
from django.db import models

# Create your models here.
'''Clase abstracta que heredará los campos de creación, actulización y estado'''

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField("status", default=True)

    class Meta:
        abstract = True 

class Customer(Base):
    """Model definition for Customer."""

    # TODO: Define fields here
    name = models.CharField('Customer name', help_text='Name', max_length=250)
    email = models.EmailField('Customer email', help_text='Customer email')
    document = models.PositiveIntegerField('Customer document', help_text='Customer document')
    birth_date = models.DateField('Customer birth date', help_text='Customer birth date')

    class Meta:
        """Meta definition for Customer."""

        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        """Unicode representation of Customer."""
        return f"{self.name} {self.email}"

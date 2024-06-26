"""
Models for contact_us app
"""
from django.db import models


class Contact(models.Model):
    """Model to represent a user contact submission"""
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=255, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    contact_date = models.DateTimeField(auto_now=True)
    replied = models.BooleanField(default=False)
    resolved = models.BooleanField(default=False)

    class Meta:
        """
        Meta class to define contact model ordering
        """
        ordering = ['-contact_date']

    def __str__(self):
        return str(self.subject)

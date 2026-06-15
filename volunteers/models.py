from django.db import models

class Volunteer(models.Model):

    SKILL_CHOICES = [
        ('Teaching', 'Teaching'),
        ('Medical', 'Medical'),
        ('Technology', 'Technology'),
        ('Marketing', 'Marketing'),
        ('Design', 'Design'),
        ('Legal', 'Legal'),
        ('Finance', 'Finance'),
        ('Other', 'Other'),
    ]

    name        = models.CharField(max_length=100)
    email       = models.EmailField(unique=True)
    phone       = models.CharField(max_length=15)
    skill       = models.CharField(max_length=50, choices=SKILL_CHOICES)
    city        = models.CharField(max_length=100)
    joined_date = models.DateField(auto_now_add=True)
    is_active   = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-joined_date']
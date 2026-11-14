from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class FirewallRequest(models.Model):
    STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Under Review', 'Under Review'),
        ('Requester Action Required', 'Requester Action Required'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    
    PROTOCOL_CHOICES = [
        ('TCP', 'TCP'),
        ('UDP', 'UDP'),
        ('ICMP', 'ICMP'),
    ]

    title = models.CharField(max_length=100)
    requester = models.CharField(max_length=100)
    source_ip = models.GenericIPAddressField()
    destination_ip = models.GenericIPAddressField()
    port = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(65535)])
    protocol = models.CharField(max_length=10, choices=PROTOCOL_CHOICES)
    justification = models.TextField()
    rule_purpose = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Submitted')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
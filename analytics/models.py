from django.db import models

class Visit(models.Model):
    session_key = models.CharField(max_length=40, db_index=True) # Django's session key
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    referrer = models.CharField(max_length=512, null=True, blank=True)
    status_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M')} - {self.path} ({self.status_code})"

    class Meta:
        ordering = ['-timestamp']
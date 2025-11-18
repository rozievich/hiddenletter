from django.db import models


# Create your models here.
class Letter(models.Model):
    content = models.CharField(max_length=800)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    ip_address = models.IPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
    
    @property
    def all_content(self):
        return self.objects.count()

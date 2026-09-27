from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=255)
    sync_time = models.DateTimeField(help_text="Time for synching")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time the timestamp was saved in")

    def __str__(self):
        return self.name

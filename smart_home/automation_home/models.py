from django.db import models

class AutomationEvent(models.Model):
    name = models.CharField(max_length=100)
    trigger = models.CharField(max_length=100)  # Ex: "som_detectado"
    action = models.CharField(max_length=100)   # Ex: "ligar_luz"
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.trigger}"

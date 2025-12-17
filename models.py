from django.db import models

class TodoItem(models.Model):
    subject = models.CharField(max_length=200)
    notes = models.TextField() # This handles the 'textarea' requirement
    
    def __str__(self):
        return self.subject

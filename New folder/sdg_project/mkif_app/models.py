# mkif_app/models.py
from django.db import models
from django.contrib.auth.models import User

class ResearchDocument(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    content = models.TextField()
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title

class InnovationProject(models.Model):
    project_name = models.CharField(max_length=200)
    participants = models.ManyToManyField(User)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    progress_update = models.TextField()

    def __str__(self):
        return self.project_name

class Communication(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver} at {self.timestamp}'

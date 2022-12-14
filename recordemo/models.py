from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile


class AddFeeling(models.Model):

    FEELING_TYPES = [
        ('happy', 'Happy'),
        ('excited', 'Excited'),
        ('calm', 'Calm'),
        ('disppointed', 'Disppointed'),
        ('anxious', 'Anxious'),
        ('angry', 'Angry'),
    ]

    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='user_feelings'
    )
    date = models.DateField(null=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    feelings = models.CharField(
        choices=FEELING_TYPES,
        null=True,
        max_length=15
    )
    details = models.TextField(null=True)

    def __str__(self):
        return self.feelings
    
    def __str__(self):
        return f"{self.user_profile}"

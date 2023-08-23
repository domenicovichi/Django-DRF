from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Profile


'''
ogni volta che un User viene salvato, manderà il segnale post_save, che verrà raccolto
dal decoratore receiver.
'''

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    print("created:", created)
    if created:
        Profile.objects.create(user = instance)
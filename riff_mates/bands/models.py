from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"Musician(id={self.id}, first_name={self.first_name}, last_name={self.last_name})"
    

class Venue (models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"Venue(id={self.id}, name={self.name})"
    

class Room(models.Model):
    name = models.CharField(max_length=20)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]
        unique_together = [["name", "venue"]]

    def __str__(self):
        return f"Room(id={self.id}, name={self.name})"
    

class Band (models.Model):
    name = models.CharField(max_length = 20)
    musicians = models.ManyToManyField(Musician)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"Band(id={self.id}, name={self.name})"
    

class UserProfile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    musician_profiles = models.ManyToManyField(Musician, blank=True)
    venues_controlled = models.ManyToManyField(Venue, blank=True)

@receiver(post_save, sender=User)
def user_post_save(sender, **kwargs):
    # Create UserProfile if Usr object is new and not loaded from fixtures
    if kwargs['created'] and not kwargs['raw']:
        user = kwargs['instance']
        try:
            # Check if UserProfile already exists
            UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=user)

@receiver(user_login_failed)
def track_login_failure(sender, **kwargs):
    username = kwargs["credentials"]["username"]
    url = kwargs["request"].path

    print(f"LOGIN Failure by {username} for {url}")
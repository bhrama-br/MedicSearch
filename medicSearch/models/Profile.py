from medicSearch.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICES, default=3)
    birthday = models.DateTimeField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)

    image = models.ImageField(null=True, blank=True)

    favorites = models.ManyToManyField(User, blank=True, related_name='favorites')
    specialties = models.ManyToManyField(Speciality, blank=True, related_name='specialties')
    addresses = models.ManyToManyField(Addresses, blank=True, related_name='addresses')

    def __str__(self):
        return '{}'.format(self.user.username)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
      try:
        if created:
          Profile.objects.create(user=instance)
      except:
        pass

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
      try:
        instance.profile.save()
      except:
        pass
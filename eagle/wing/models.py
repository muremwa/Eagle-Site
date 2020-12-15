from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class EagleProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    portrait = models.ImageField(upload_to='eagle_details/')
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    email = models.EmailField()
    objects = models.Manager()

    class Meta:
        verbose_name = 'Super Profile'
        verbose_name_plural = 'Eagle Profile'

    @staticmethod
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            if instance.is_superuser:
                EagleProfile.objects.create(user=instance)

    def __str__(self):
        return f"EAGLE PROFILE FOR {str(self.user.username).upper()}"


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    portfolio_type = models.CharField(max_length=300)
    image = models.ImageField(upload_to='portfolio/portfolio_images/')
    description = models.TextField()
    link = models.URLField()
    github_link = models.URLField(blank=True, null=True)
    download_stats = models.URLField(blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.title


class UserMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=400)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return "Message from {}".format(self.name)


# experiences in work
class EagleExperience(models.Model):
    company = models.CharField(max_length=100, help_text="Where did you work?")
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    started = models.DateField(blank=False, null=False)
    ended = models.DateField(
        blank=True,
        null=True,
        help_text="If you leave this blank it will indicate that you still work here",
    )
    objects = models.Manager()

    class Meta:
        ordering = ('-started',)

    def __str__(self):
        if self.ended:
            to_date = self.ended
        else:
            to_date = "Present"

        return "Experience at {company} from {from_date} to {to_date}".format(
            company=self.company,
            from_date=self.started,
            to_date=to_date,
        )


# Education experience
class EagleEducation(models.Model):
    school = models.CharField(max_length=50, help_text="What institution were you in?")
    qualification = models.CharField(max_length=50, help_text="What did you achieve?")
    location = models.CharField(max_length=100)
    started = models.DateField(blank=False, null=False)
    ended = models.DateField(
        blank=True,
        null=True,
        help_text="If you leave this blank it will indicate that you are a continuing student",
    )
    objects = models.Manager()

    class Meta:
        verbose_name = "Eagle education experience"
        verbose_name_plural = "Eagle education experiences"
        ordering = ('-started',)

    def __str__(self):
        if self.ended:
            to_date = self.ended
        else:
            to_date = "Present"

        return "Education at {school} from {from_date} to {to_date}".format(
            school=self.school,
            from_date=self.started,
            to_date=to_date,
        )

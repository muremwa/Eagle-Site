from django.db import models


class EagleDetails(models.Model):
    bio = models.TextField()
    portrait = models.ImageField(upload_to='eagle_details/')
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=10)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    email = models.EmailField()
    website = models.URLField()
    objects = models.Manager()

    class Meta:
        verbose_name = 'Super Details'
        verbose_name_plural = 'Eagle Details'

    def __str__(self):
        return "EAGLE DETAILS"


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    portfolio_type = models.CharField(max_length=300)
    image = models.ImageField(upload_to='portfolio/portfolio_images/')
    description = models.TextField()
    link = models.URLField()
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


class EagleExperience(models.Model):
    company = models.CharField(max_length=100, help_text="Where did you work?")
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    started = models.DateField(blank=False, null=False)
    ended = models.DateField(
        blank=True,
        null=True,
        help_text="If you leave this blank it will indicate that you still work here"
    )
    objects = models.Manager()

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

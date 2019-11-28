from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse

# authors of a post
class Author(models.Model):
    name = models.CharField(max_length=500, help_text="Enter Full name")
    about = models.TextField(help_text="Bio")
    avatar = models.ImageField(
        upload_to='blog/authors_avatars/',
        default='blog/default_images/default_author_avatar.png'
    )

    def __str__(self):
        return "Author called {}".format(self.name)


# tag the post
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Tag for {}".format(self.name)


# Each blog post
class Post(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    feature_image = models.ImageField(
        upload_to="blog/feature_images",
        default="blog/default_images/default_feature.png"
    )
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return "Blog post titled {}".format(self.title)

    def get_date(self):
        return self.created.date().strftime("%B %d, %Y")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save()

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={
            'slug':self.slug,
        })


# each entry
class Entry(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    heading = models.CharField(max_length=50, help_text="This is not a must", blank=True, null=True)
    content = models.TextField(help_text="Entry here")
    image = models.ImageField(upload_to="blog/entry_images", blank=True, null=True)

    def __str__(self):
        if self.heading:
            return "{entry_title} (Entry) from the {post}".format(
                entry_title=self.heading,
                post=str(self.post).lower()
            )
        else:
            return "Entry from a {}".format(str(self.post).lower())


# Comments for each post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, help_text="Enter your full name")
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return "Comment by {owner} on a {post}".format(post=str(self.post).lower(), owner=self.name)

    def get_date(self):
        return self.created.strftime("%B %d, %Y at %H:%M%p")

    def get_absolute_url(self):
        return "{post_url}#comment-{comment_pk}".format(
            comment_pk=self.pk,
            post_url=self.post.get_absolute_url()[:-1],
        )

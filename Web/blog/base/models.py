import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.core.validators import RegexValidator, MinLengthValidator, ValidationError
from ckeditor.fields import RichTextField
from blog import settings
from datetime import date

category_n_title_min_len = MinLengthValidator(3, 'Minimum length of 3 letters required.')
letters_n_whitespaces = RegexValidator(r'^[a-zA-Z ]*$', 'Only alphabet characters are allowed.')
location_name_validator = RegexValidator(r'^[0-9a-zA-Z ,-]*$',
                                         "Only alphanumeric, '-', ',' and whitespace characters are allowed.")
location_len_validator = MinLengthValidator(15, 'Minimum length of 15 letters required.')


def no_present_nor_future(value):
    today = date.today()
    if value >= today:
        raise ValidationError('Date cannot be present or in the future.')


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[letters_n_whitespaces, category_n_title_min_len])

    class Meta:
        verbose_name = 'Category'  # the name of the model class in the admin list section.
        verbose_name_plural = 'Categories'  # the name of the model class in the main admin page.
        ordering = ('name',)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[letters_n_whitespaces, category_n_title_min_len])
    # many-2-one relationship where post = one and user = many. Place FK in the 'many' model.
    # default reverse relationship by user.post_set
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    # auto_now_add sets the date when the post is created. It cannot be overridden.
    # auto_now sets the date every time the obj is updated/saved. It cannot be overridden.
    date_published = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, help_text='Select a category for this post.')
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    snippet = models.CharField(max_length=100)

    class Meta:
        ordering = ('-date_published',)

    def likes_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    # get_abs_url returns a link pointing to an obj instance
    # {% url 'post-detail' obj.pk %} == {{ obj.get_absolute_url }}
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.pk)])


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.PROTECT)
    name = models.CharField(max_length=100, validators=[letters_n_whitespaces, category_n_title_min_len])
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username


class Profile(models.Model):
    # CASCADE deletes the reference object.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='profile/images/')
    location = models.CharField(max_length=100, blank=True, validators=[location_name_validator, location_len_validator])
    birth_date = models.DateField(null=True, blank=True, help_text='YYYY-MM-DD', validators=[no_present_nor_future])
    bio = models.TextField(blank=True)
    # URLfield = Charfield + URLvalidator
    facebook_url = models.URLField(max_length=255, null=True, blank=True)
    linkedin_url = models.URLField(max_length=255, null=True, blank=True)
    instagram_url = models.URLField(max_length=255, null=True, blank=True)
    twitter_url = models.URLField(max_length=255, null=True, blank=True)
    github_url = models.URLField(max_length=255, null=True, blank=True)

    def get_facebook_url(self):
        if self.facebook_url:
            return self.facebook_url
        return '#'

    def get_linkedin_url(self):
        if self.linkedin_url:
            return self.linkedin_url
        return '#'

    def get_instagram_url(self):
        if self.instagram_url:
            return self.instagram_url
        return '#'

    def get_twitter_url(self):
        if self.twitter_url:
            return self.twitter_url
        return '#'

    def get_github_url(self):
        if self.github_url:
            return self.github_url
        return '#'

    def get_profile_picture(self):
        if self.profile_picture:
            return self.profile_picture.url
        directory = os.path.join(settings.STATIC_URL, 'images/default.jpg')
        return directory

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.pk)])


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

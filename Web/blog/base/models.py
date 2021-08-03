from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse
# slugify turns our post title into a slug
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Category'  # the name of the model class in the admin list section.
        verbose_name_plural = 'Categories'  # the name of the model class in the main admin page.

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    # many-2-one relationship where post = one and user = many. Place FK in the 'many' model.
    # default reverse relationship by user.post_set
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    # auto_now_add sets the date when the post is created. It cannot be overridden.
    # auto_now sets the date every time the obj is updated/saved. It cannot be overridden.
    date_published = models.DateTimeField(auto_now_add=True)
    # category = models.CharField(max_length=255, default='no category')
    category = models.ManyToManyField(Category, help_text='Select a category for this post.')
    # slug = models.SlugField(max_length=250, unique=True)

    # TODO:
    # date_created
    # date_updated

    # published (boolean)
    # tags

    def __str__(self):
        # return self.title + ' by ' + self.author.username
        return self.title

    # get_abs_url returns a link pointing to an obj instance
    # {% url 'post-detail' obj.pk %} == {{ obj.get_absolute_url }}
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.pk)])


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # TODO:
    # likes and dislikes + list users who liked/disliked (dropdown or new page)

    def __str__(self):
        return self.author.username

# def check_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Post.objects.filter(slug=slug).order_by('-pk')
#     exists = qs.exists()
#     if exists:
#         # new_slug = f'{slug}-{qs.first().pk}'
#         new_slug = "%s-%s" % (slug, qs.first().pk)
#         return create_slug(instance, new_slug=new_slug)
#     return slug

# anytime save() is called, the function create_slug will be called to update the slug accordingly
# before the actual save in the database
# "apple m1" -> "apple-m1" -> "apple-m1-pk"


# @receiver(pre_save, sender=Post)
# def create_slug(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = check_slug(instance)


class Profile(models.Model):
    # CASCADE deletes the reference object.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    bio = models.TextField(blank=True)

    # TODO:
    # profile_picture

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

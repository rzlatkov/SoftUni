from django.contrib import admin
from .models import Post, Profile, Category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published', 'get_category')
    list_filter = ('date_published', 'category')
    search_fields = ('title', 'category__name', 'author__username')

    # navigation
    date_hierarchy = 'date_published'

    # display up to three categories for a given post instance
    def get_category(self, obj):
        cats = [cat.name for cat in obj.category.all()[:3]]
        cats = ', '.join(cats)
        return cats

    # the column name representation of the custom method above.
    get_category.short_description = 'Category'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_full_name', 'get_email', 'location', 'birth_date')
    list_filter = ('user__username', 'birth_date', 'location')
    ordering = ('user__username',)
    search_fields = ('user__username', 'location')

    def get_email(self, obj):
        return obj.user.email

    def get_username(self, obj):
        return obj.user.username

    def get_full_name(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

    get_email.short_description = 'email'
    get_username.short_description = 'user'
    get_full_name.short_description = 'full name'


# the admin interface has the ability to edit models on the same page as a parent model.
class PostsInline(admin.TabularInline):
    model = Post.category.through
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [PostsInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    def custom_titled_filter(title):
        class Wrapper(admin.FieldListFilter):
            def __new__(cls, *args, **kwargs):
                instance = admin.FieldListFilter.create(*args, **kwargs)
                instance.title = title
                return instance
        return Wrapper

    list_display = ('get_by_username', 'get_to_username', 'get_post_title', 'date_published', 'date_modified',)
    list_filter = ('date_published', 'date_modified',
                   ('author__username', custom_titled_filter('From')),
                   ('post__author__username', custom_titled_filter('To')),)

    ordering = ('author__username',)
    search_fields = ('author__username', 'post__author__username', 'post__title',)

    def get_by_username(self, obj):
        return obj.author.username

    def get_to_username(self, obj):
        return obj.post.author.username

    def get_post_title(self, obj):
        return obj.post.title

    get_by_username.short_description = 'from'
    get_to_username.short_description = 'to'
    get_post_title.short_description = 'post title'

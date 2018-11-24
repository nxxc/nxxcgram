from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from nxxcgram.users import models as user_models
from taggit.managers import TaggableManager
from django.contrib.humanize.templatetags.humanize import naturaltime
# Create your models here


@python_2_unicode_compatible
class TimeStampedModel(models.Model):

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

@python_2_unicode_compatible
class Image(TimeStampedModel):

    """ Image model """
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True, related_name='images')
    tags = TaggableManager()

    @property
    def like_count(self):
        return self.likes.all().count()

    @property
    def comment_count(self):
        return self.comments.all().count()

    @property
    def natural_time(self):
        return naturaltime(self.created_at)

    def __str__(self):
        return '{}-{}'.format(self.location, self.caption)

    class Meta:
        ordering = ['-created_at']


@python_2_unicode_compatible
class Comment(TimeStampedModel):

    """ Comment model """
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name='comments')

    def __str__(self):
        return self.message


@python_2_unicode_compatible
class Like(TimeStampedModel):

    """ Like model """

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name='likes')

    def __str__(self):
        return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption)

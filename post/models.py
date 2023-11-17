from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):

    """
    in this model we need a title and cover and description
    and we show the model on app pages but we create on this app
    """

    title = models.CharField(_("Title"), max_length=50)
    # cover
    description = models.TextField(_("Description"))
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})

from django.db import models

from base.models import Anchor


class PlatformProfile(models.Model):
    """Link to a social profile."""

    anchor_profile = models.OneToOneField(Anchor, null=True, on_delete=models.SET_NULL)

    url = models.URLField(
        max_length=500,
        help_text='Link to profile.',
        blank=True,
        null=True,
    )

    FACEBOOK = 'Facebook'
    TWITTER = 'Twitter'
    INSTAGRAM = 'Instagram'
    REDDIT = 'Reddit'
    TIKTOK = 'TikTok'
    TUMBLR = 'Tumblr'
    YOUTUBE = 'YouTube'
    VIMEO = 'Vimeo'
    PINTEREST = 'Pinterest'
    TWITCH = 'Twitch'
    PLATFORM_CHOICES = (
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (INSTAGRAM, 'Instagram'),
        (REDDIT, 'Reddit'),
        (TIKTOK, 'TikTok'),
        (TUMBLR, 'Tumblr'),
        (YOUTUBE, 'YouTube'),
        (VIMEO, 'Vimeo'),
        (PINTEREST, 'Pinterest'),
        (TWITCH, 'Twitch'),
    )

    platform = models.CharField(
        max_length=25,
        choices=PLATFORM_CHOICES,
        help_text='Platform of profile.'
    )

    class Meta:
        verbose_name = 'Platform Profile'
        verbose_name_plural = "Platform Profiles"
        ordering = ['anchor_profile']

    def __str__(self):
        return "{{ anchor type }} {{ anchor }} {{ platform }} profile".format(
            anchor = self.anchor_profile.anchor_name,
            anchor_type=self.anchor_profile.anchor_type,
            platform = self.platform,
        )

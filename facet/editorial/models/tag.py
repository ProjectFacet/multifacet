from django.db import models

class Tag(models.Model):
    """Tag for content.

    Tags are associated with
    Project
    Story
    Item
    ImageAsset
    DocumentAsset
    AudioAsset
    VideoAsset
    """

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.CharField(
        max_length=150,
        help_text = 'Simple tag to find and collect content.',
    )

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = "Tags"
        ordering = ['text']

    def __str__(self):
        return self.text

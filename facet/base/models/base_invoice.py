from django.db import models

class BaseInvoice(models.Model):
    """Invoice for freelance assignment(s)"""

    reference_code = models.CharField(
        max_length=300,
        help_text='Text or numberic short identifier for Invoice.',
    )

    text = models.TextField(
        help_text='Details of the invoice.',
    )

    total_due = models.IntegerField(
        max_length=100,
        help_text='Total value of the invoice.',
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Day assignment was created.',
        blank=True,
    )

    submitted = models.BooleanField(
        default=False,
        help_text='Invoice has been submitted.',
    )

    submitted_date = models.DateTimeField(
        auto_now_add=False,
        help_text='Datetime invoice was submitted to talent editor.',
        blank=True,
    )

    under_review = models.BooleanField(
        default=False,
        help_text='Invoice is under review by Freelance Manager/News Organization.',
    )

    paid = models.BooleanField(
        default=False,
        help_text='Payment has been remitted for this assignment.',
    )

    payment_submitted_date = models.DateTimeField(
        auto_now_add=False,
        help_text='Datetime payment was remitted or scheduled to remit to freelancer.',
        blank=True,
    )

    # simple assets
    simple_image_assets = models.ManyToManyField(SimpleImage, blank=True)
    simple_document_assets = models.ManyToManyField(SimpleDocument, blank=True)
    simple_audio_assets = models.ManyToManyField(SimpleAudio, blank=True)
    simple_video_assets = models.ManyToManyField(SimpleVideo, blank=True)

    class Meta:
        abstract = True
        ordering = ['creation_date']

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

    total_due = models.DecimalField(
        help_text='Total value of the invoice.',
        max_digits=8,
        decimal_places=2,
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

    # internal assets
    internal_image_assets = models.ManyToManyField('internalasset.InternalImage', blank=True)
    internal_document_assets = models.ManyToManyField('internalasset.InternalDocument', blank=True)
    internal_audio_assets = models.ManyToManyField('internalasset.InternalAudio', blank=True)
    internal_video_assets = models.ManyToManyField('internalasset.InternalVideo', blank=True)

    class Meta:
        abstract = True
        ordering = ['creation_date']

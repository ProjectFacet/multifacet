from django.contrib.postgres.fields import ArrayField
# from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.utils.encoding import python_2_unicode_compatible
# from simple_history.models import HistoricalRecords

# from . import User, Organization, Story
from . import Story
# from .discussion import Discussion


#-----------------------------------------------------------------------#
#   ITEM
#-----------------------------------------------------------------------#

class ItemTemplate(models.Model):
    """Template for items.

    A template is a collection of fields so that when adding/editing an item,
    only appropriate fields are shown.
    """

    name = models.CharField(
        max_length=50,
    )

    # A template without an organization is a "site-wide" template;
    # when listing templates for an organization, list the site-wide and
    # ones that match the organization.
    # organization = models.ForeignKey(
    #     "Organization",
    #     blank=True,
    #     null=True,
    # )
    #
    # owner = models.ForeignKey(
    #     "User",
    #     blank=True,
    #     null=True,
    # )

    description = models.CharField(
        max_length=100,
        blank=True,
    )

    fields_used = ArrayField(
        models.CharField(max_length=50),
        default=list,
        help_text='Fields used by this template.',
        blank=True,
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        help_text='When template was created.',
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ['id']
        # unique_together = ['name', 'organization']

    def __str__(self):
        return self.name

    @property
    def search_title(self):
        return self.name

    @property
    def type(self):
        return "Item Template"


    def copy(self):
        """ Create a copy of an item template for a partner organization in a network."""

        print("in item template copy")
        self.id = None
        self.is_active=False
        print("pre copy save")
        self.save()
        print("saved")
        print("new id", self.id)
        return self

    def get_absolute_url(self):
        if self.organization:
            return reverse('item_template_edit', kwargs={'template': self.id, 'org': self.organization.id})
        else:
            return reverse('item_template_detail', kwargs={'template': self.id})


# field which will appear on all item-editing forms -- and therefore do not
# need to be in the "fields_used" for a template.

COMMON_FIELDS = {
    "name",
    "headline",
    "description",
    "editor",
    "credit",
    # "team",
    "content",
    "status",
    "due_edit",
    "run_date",
    "keywords",
    # "template",
    # "story",
}


class Item(models.Model):
    """A version of a story.

    An item must belong to a story and can only belong to one story. An item is a version
    of the story.

    Ex. A story about wildfires could have:
    - a web story item that is a text article with photos and video
    - a host-wrap item that is the radio script of a story about the fire
    - a video item that is a video segment about the fire for distribution via social media.
    - an item that is a version of the story in a different language.
    """

    # ------------------------#
    # required fields
    # ------------------------#

    # populated during save
    # owner = models.ForeignKey(
    #     User,
    #     related_name='itemowner'
    # )
    #
    # organization = models.ForeignKey(
    #     Organization,
    #     help_text='Organization that owns this item.'
    # )

    template = models.ForeignKey(
        ItemTemplate,
        on_delete = models.SET_DEFAULT,
        default=1,
    )

    story = models.ForeignKey(
        Story,
        on_delete = models.SET_NULL,
        null=True,
    )

    original = models.BooleanField(
        default=True,
        help_text='Was this item originally created by a user from this organization?',
        # If item is not original, set to false and use ItemCopyDetail for additional info.
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Day item was created.',
        blank=True,
    )

    # discussion = models.ForeignKey(
    #     'Discussion',
    #     help_text='Id of discussion for the item.',
    #     blank=True,
    #     null=True,
    # )

    # populated by user
    name = models.TextField(
        # displayed on form as label
        help_text='Internal name for item.'
    )

    headline = models.TextField(
        help_text='Headline of the item',
    )

    description = models.TextField(
        help_text='Description of the item.',
        blank=True,
    )

    # editor = models.ManyToManyField(
    #     User,
    #     related_name='itemeditor',
    #     help_text='The full user name(s) to be listed as the editor(s) for the item.',
    #     blank=True,
    #     on_delete = models.SET_NULL,
    # )
    #
    # credit = models.ManyToManyField(
    #     User,
    #     related_name='itemcredit',
    #     help_text='The full user name(s) to be listed as the credit for the item.',
    #     blank=True,
    #     on_delete = models.SET_NULL,
    # )
    #
    # team = models.ManyToManyField(
    #     User,
    #     through='ItemContributor',
    #     help_text='Users that contributed to an item. Used to associate multiple users to an item.',
    #     blank=True,
    #     on_delete = models.SET_NULL,
    # )

    content = models.TextField(
        help_text='Content of the item.',
        blank=True,
    )

    # Choices for item status.
    DRAFT = 'Draft'
    PITCH = 'Pitch'
    IN_PROGRESS = 'In Progress'
    EDIT = 'Edit'
    REVISION = 'Revision'
    NEEDS_REVIEW = 'Needs Review'
    READY = 'Ready'
    ITEM_STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PITCH, 'Pitch'),
        (IN_PROGRESS, 'In Progress'),
        (EDIT, 'Edit'),
        (REVISION, 'Revision'),
        (NEEDS_REVIEW, 'Needs Review'),
        (READY, 'Ready'),
    )

    status = models.CharField(
        max_length=25,
        choices=ITEM_STATUS_CHOICES,
        help_text='Item status choice.'
    )

    due_edit = models.DateTimeField(
        help_text='Due for edit.',
        blank=True,
        null=True,
    )

    run_date = models.DateTimeField(
        help_text='Planned run date.',
        blank=True,
        null=True,
    )

    keywords = ArrayField(
        models.CharField(max_length=100),
        default=list,
        help_text='List of keywords for search.',
        blank=True,
    )

    # assets
    # image_assets = models.ManyToManyField(
    #     'ImageAsset',
    #     blank=True,
    # )
    #
    # document_assets = models.ManyToManyField(
    #     'DocumentAsset',
    #     blank=True,
    # )
    #
    # audio_assets = models.ManyToManyField(
    #     'AudioAsset',
    #     blank=True,
    # )
    #
    # video_assets = models.ManyToManyField(
    #     'VideoAsset',
    #     blank=True,
    # )

    # history
    # edit_history = HistoricalRecords()

    # ------------------------#
    # optional fields
    # ------------------------#

    update_note  = models.TextField(
        help_text='Text commenting regarding any updates or corrections made to the item.',
        blank=True,
    )

    excerpt = models.TextField(
        help_text='Excerpt from the item.',
        blank=True,
    )

    dateline = models.CharField(
        max_length=150,
        help_text='Where and when the item was created.',
        blank=True,
    )

    share_note = models.TextField(
        help_text='Information for organizations making a copy of the item.',
        blank=True,
    )

    topic_code = models.CharField(
        max_length=75,
        help_text='Unique code as needed to designate topic or coverage.',
        blank=True,
    )

    internal_code = models.CharField(
        max_length=75,
        help_text='Unique code as needed for ingest sytems or internal use. Use as needed.',
        blank=True,
    )

    length = models.CharField(
        max_length=75,
        help_text='Length of item for audio or video.',
        blank=True,
    )

    wordcount = models.CharField(
        max_length=75,
        help_text='Wordcount for text-based items.',
        blank=True,
    )

    content_license = models.ForeignKey(
        'ContentLicense',
        related_name='itemlicense',
        blank=True,
        null=True,
        on_delete = models.SET_NULL,
    )

    related_links = models.TextField(
        help_text='Relevant links that can be included with the item.',
        blank=True,
    )

    github_link = models.URLField(
        max_length=300,
        help_text='Link to code for any custom feature.',
        blank=True,
    )

    sources = models.TextField(
        help_text='List of sources in the item.',
        blank=True,
    )

    edit_note = models.TextField(
        help_text='Information regarding allowable extent of editing and suggestions for specific kinds of edits.',
        blank=True,
    )

    pronounciations = models.TextField(
        help_text='Information about pronouncing names or potentially difficult words.',
        blank=True,
    )

    sponsors = models.TextField(
        help_text='Sponsors or underwriters if need to indicate any.',
        blank=True,
    )

    # ------------------------#
    #   web specific fields
    # ------------------------#

    # also relevant for print
    pull_quotes = models.TextField(
        help_text='List of quotes and attributions to be used as pull quotes.',
        blank=True,
    )

    embeds = models.TextField(
        help_text='The necessary information to embed something like a Tweet, FB post, map or video.',
        blank=True,
    )

    # push to CMS history
    # pushed_to_wp = models.BooleanField(
    #     default=False,
    #     help_text='Whether the item has been pushed to the organization WordPress site.',
    # )

    # ------------------------#
    # print specific fields
    # ------------------------#

    sidebar_content = models.TextField(
        help_text='Content separate from body text meant for sidebar or inset presentation.',
        blank=True,
    )

    # ------------------------#
    # audio specific fields
    # ------------------------#

    # relevant for video
    # producer = models.ForeignKey(
    #     User,
    #     related_name='itemproducer',
    #     blank=True,
    #     null=True,
    # )

    # ------------------------#
    # tv and video specific
    # ------------------------#

    series_title = models.TextField(
        help_text='Title of the video series.',
        blank=True,
    )

    episode_number = models.CharField(
        max_length=75,
        help_text='If the video is part of a series, the episode number.',
        blank=True,
    )

    usage_rights = models.TextField(
        help_text='Information regarding the usage of the video if shared.',
        blank=True,
    )

    tape_datetime = models.DateTimeField(
        help_text='Tape date.',
        blank=True,
        null=True,
    )

    locations = models.TextField(
        help_text='Shoot locations.',
        blank=True,
    )

    # ------------------------#
    # user defined fields
    # ------------------------#

    custom_one = models.TextField(
        help_text='User-defined field.',
        blank=True,
    )

    custom_two = models.TextField(
        help_text='User-defined field.',
        blank=True,
    )

    custom_three = models.TextField(
        help_text='User-defined field.',
        blank=True,
    )

    custom_four = models.TextField(
        help_text='User-defined field.',
        blank=True,
    )

    custom_five = models.TextField(
        help_text='User-defined field.',
        blank=True,
    )

    class Meta:
        verbose_name='Item'
        verbose_name_plural='Items'
        # ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item_edit', kwargs={'pk': self.id, 'story': self.story_id})

    # def copy(self):
    #     """ Create a copy of an item for a partner organization in a network."""
    #
    #     self.id = None
    #     self.original=False
    #     self.code = ''
    #     self.status= 'NR'
    #     self.due_edit = None
    #     self.run_date = None
    #     self.discussion = Discussion.objects.create_discussion("F")
    #     # self.edit_history = HistoricalRecords()
    #     print "pre copy save"
    #     self.save()
    #     print "saved"
    #     print "new id", self.id
    #     return self
    #
    # def get_item_images(self):
    #     """Retrieve all images objects associated with an item."""
    #
    #     return self.image_assets.all()
    #
    # def get_item_documents(self):
    #     """Retrieve all documents objects associated with an item."""
    #     return self.document_assets.all()
    #
    # def get_item_audio(self):
    #     """Retrieve all audio objects associated with an item."""
    #     return self.audio_assets.all()
    #
    # def get_item_video(self):
    #     """Retrieve all video objects associated with an item."""
    #     return self.video_assets.all()
    #
    # def get_item_download(self):
    #     """ Return rst formatted string for downloading item and its meta."""
    #
    #     # loop over m2m and get the values as string
    #     credits = self.credit.all()
    #     credits = [ user.credit_name for user in credits]
    #     credits = ", ".join(credits)
    #
    #     editors = self.editor.all()
    #     editors = [ user.credit_name for user in editors]
    #     editors = ", ".join(editors)
    #
    #     # loop over m2m and get the values as string
    #     images = self.image_assets.all()
    #     images = [image.title for image in images]
    #     images = ", ".join(images)
    #
    #     # loop over m2m and get the values as string
    #     documents = self.document_assets.all()
    #     documents = [document.title for document in documents]
    #     documents = ", ".join(documents)
    #
    #     # loop over m2m and get the values as string
    #     audiofiles = self.audio_assets.all()
    #     audiofiles = [audiofile.title for audiofile in audiofiles]
    #     audiofiles = ", ".join(audiofiles)
    #
    #     # Loop over m2m and get the values as string
    #     videos = self.video_assets.all()
    #     videos = [video.title for video in videos]
    #     videos = ", ".join(videos)
    #
    #     # verify the text area fields have correct encoding
    #     name = self.name.encode('utf-8')
    #     description = self.description.encode('utf-8')
    #     excerpt = self.excerpt.encode('utf-8')
    #     share_note = self.share_note.encode('utf-8')
    #     content = self.content.encode('utf-8')
    #
    #     item_download = """
    #     Item\r\n
    #     ========\r\n
    #     {name}\r\n
    #     --------------\r\n
    #     Description: {desc}\r\n
    #     Story: {story}\r\n
    #     Owner: {owner}\r\n
    #     Organization: {organization}\r\n
    #     Original: {original}\r\n
    #     Editor: {editor}\r\n
    #     Credit: {credit}\r\n
    #     Code: {code}\r\n
    #     Excerpt: {excerpt}\r\n
    #     Keywords: {keywords}\r\n
    #     Status: {status}\r\n
    #     Due Edit: {dueedit}\r\n
    #     Run Date: {rundate}\r\n
    #     Share Note: {sharenote}\r\n
    #     Images: {images}\r\n
    #     Documents: {documents}\r\n
    #     AudioFiles: {audiofiles}\r\n
    #     Videos: {videos}\r\n
    #     \r\n
    #     Content\r\n
    #     -------\r\n
    #     {content}
    #     """.format(name=name, desc=description, story=self.story, owner=self.owner,
    #     organization=self.organization.name, original=self.original, editor=editors,
    #     credit=credits, code=self.internal_code, excerpt=excerpt,
    #     keywords=self.keywords, status=self.status, dueedit=self.due_edit, rundate=self.run_date,
    #     sharenote=share_note, images=images, documents=documents, audiofiles=audiofiles, videos=videos, content=content)
    #
    #     return item_download

    @property
    def search_title(self):
        return self.name

    @property
    def type(self):
        return "Item"

#     def is_editable_by_org(self, org):
#         """Can this item be edited by this org?"""
#
#         # FIXME: add contractor access?
#
#         story = self.organization
#
#         return (org == story.organization or
#                 (story.collaborate and org in story.collaborate_with.all()))
#
#
# @receiver(post_save, sender=Item)
# def add_discussion(sender, instance, **kwargs):
#     if not instance.discussion:
#         instance.discussion = Discussion.objects.create_discussion("F")
#         instance.save()



#-----------------------------------------------------------------------#
#   ItemContributor
#-----------------------------------------------------------------------#

# class ItemContributor(models.Model):
#     """ Which users are participating in creating the item. """
#
#     item = models.ForeignKey(
#         Item,
#     )
#
#     user = models.ForeignKey(
#         User,
#     )
#
#     user_role = models.CharField(
#         max_length=255,
#         help_text='What did the user do?',
#     )
#
#     def __str__(self):
#         return "{item}, {contributor}".format(
#                                         item=self.item.name,
#                                         contributor=self.user.credit_name,
#                                         )

#-----------------------------------------------------------------------#
#   CONTENT LICENSE
#-----------------------------------------------------------------------#

class ContentLicense(models.Model):
    """Content License for items.

    Items can have a related content license. The data for this model
    includes the 7 established variations of the Creative Commons license;
    these have a blank Organization field.

    Organizations can also create their own content licenses/reuse terms and
    upload documents for the custom license.
    """

    name = models.TextField(
        help_text='Name for the license.',
    )

    # organization = models.ForeignKey(
    #     Organization,
    #     null=True,
    #     blank=True,
    #     help_text='Organization that owns this license.',
    # )

    terms = models.TextField(
        help_text='Content of the terms.',
        blank=True,
    )

    upload = models.FileField(
        upload_to="license/%Y/%m/%d/",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Content License'
        verbose_name_plural = 'Content Licenses'
        ordering = ['name']

    def __str__(self):
        return self.name

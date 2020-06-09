"""Item Views for Item/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from editorial.forms import (
    ItemTemplateForm,
    ItemPreCreateForm,
    get_item_form_for_template,
    ImageAssetForm,
    DocumentAssetForm,
    AudioAssetForm,
    VideoAssetForm,
)

from editorial.models import (
    Project,
    Story,
    Item,
    ItemTemplate,
    ImageAsset,
    DocumentAsset,
    AudioAsset,
    VideoAsset,
)

from communication.models import (
    Discussion,
    Comment,
)


class ItemPreCreateView(FormMessagesMixin, FormView):
    """First step in creating an item."""

    form_class = ItemPreCreateForm
    template_name = 'item/item_precreate_form.html'

    form_invalid_message = "Something went wrong."
    form_valid_message = "Item started. Add a status, headline and content to get started."

    def get_form_kwargs(self):
        """Pass existing/future entity_owner to the form."""

        participant = self.request.user

        kw = super(ItemPreCreateView, self).get_form_kwargs()
        #if staffjournalist, pass NewsOrganization
        if participant.staffjournalist:
            kw.update({'entity_owner': participant.staffjournalist.newsorganization})
            kw.update({'participant_owner': self.request.user})
        # if unaffiliated or freelance, no entity_owner
        elif participant.unaffiliatedstaffjournalist:
            kw.update({'participant_owner': self.request.user})
        elif participant.freelancejournalist:
            kw.update({'participant_owner': self.request.user})
        else:
            kw.update({'entity_owner': None})
            kw.update({'participant_owner': None})
        return kw

    def form_valid(self, form):
        """Redirect to real item-creation form."""

        template = form.data['template']
        name = form.cleaned_data['name']

        url = reverse("item_add",
                      kwargs={'template_id': template, 'story': self.kwargs['story']})
        return redirect("{}?name={}".format(url, name))


class ItemCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """Create an item (dynamically using right template)."""

    model = Item
    template_name = 'item/item_form.html'

    form_invalid_message = "Something went wrong."
    form_valid_message = "Item created."

    def get_form_class(self):
        """Get dynamic form, based on this template."""

        return get_item_form_for_template(self.kwargs['template_id'])

    def get_form_kwargs(self):
        """Pass some initial things to scaffold form."""

        kwargs = super(ItemCreateView, self).get_form_kwargs()
        kwargs['template'] = ItemTemplate.objects.get(pk=self.kwargs['template_id'])
        kwargs['story'] = Story.objects.get(pk=self.kwargs['story'])
        #if staffjournalist, pass NewsOrganization
        if self.request.user.staffjournalist:
            kw.update({'entity_owner': self.object.request.user.staffjournalist.newsorganization})
        # if unaffiliated or freelance, no entity_owner
        if self.request.user.unaffiliatedstaffjournalist:
            kw.update({'participant_owner': self.request.user})
        if self.request.user.freelancejournalist:
            kw.update({'participant_owner': self.request.user})
        return kwargs

    def get_initial(self):
        """Initial data for form:
        - name (optionally, from request data)
        """

        template = ItemTemplate.objects.get(pk=self.kwargs['template_id'])

        return {'name': self.request.GET.get('name', ''), 'template': template, 'content': 'Content here', 'status': 'Draft'}


class ItemUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """Update an item (dynamically using right template)."""

    model = Item
    template_name = 'item/item_form.html'
    form_invalid_message = "Something went wrong."
    form_valid_message = "Changes saved."

    def get_form_class(self):
        """Get dynamic form based on this template."""

        return get_item_form_for_template(self.object.template_id)

    # FIXME account for multiple discussions associated with anchor profile
    # def item_discussion(self):
    #     """Get discussion, comments and comment form for the item."""
    #
    #     self.object = self.get_object()
    #     discussion = self.object.discussion
    #     comments = discussion.comment_set.all().order_by('date')
    #     form = CommentForm()
    #     return {'discussion': discussion, 'comments': comments, 'form': form}

    def item_image_assets(self):
        """Return all image assets associated with an item and the forms to associate more."""

        self.object = self.get_object()
        images = self.object.get_item_images()
        image_library = self.object.get_image_library()
        uploadform = ImageAssetForm()
        return {'images': images, 'image_library': image_library, 'uploadform': uploadform}

    def item_document_assets(self):
        """Return all document assets associated with an item and the forms to associate more."""

        self.object = self.get_object()
        documents = self.object.get_item_documents()
        document_library = self.object.get_document_library()
        uploadform = DocumentAssetForm()
        return {'documents': documents, 'document_library': document_library, 'uploadform': uploadform}

    def item_audio_assets(self):
        """Return all audio assets associated with an item and the forms to associate more."""

        self.object = self.get_object()
        audio = self.object.get_item_audio()
        audio_library = self.object.get_audio_library()
        uploadform = AudioAssetForm()
        return {'audio': audio, 'audio_library': audio_library, 'uploadform': uploadform}

    def item_video_assets(self):
        """Return all video assets associated with an item and the forms to associate more."""

        self.object = self.get_object()
        videos = self.object.get_item_video()
        video_library = self.object.get_video_library()
        uploadform = VideoAssetForm()
        return {'videos': videos, 'video_library': video_library, 'uploadform': uploadform}

    def item_kwargs(self):
        """Return kwargs from url for navigation."""
        item_kwargs = self.kwargs['pk']
        return item_kwargs


class ItemDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """View for handling deletion of an item.

    In this project, we expect deletion to be done via a JS pop-up UI; we don't expect to
    actually use the "do you want to delete this?" Django-generated page. However, this is
    available if useful.
    """

    model = Item
    template_name = "item/item_delete.html"

    form_valid_message = "Deleted."
    form_invalid_message = "Please check form."

    def get_success_url(self):
        """Post-deletion, return to the story URL."""

        return Story.objects.get(pk=self.kwargs['story']).get_absolute_url()

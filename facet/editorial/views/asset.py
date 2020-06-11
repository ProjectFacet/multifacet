"""Asset Views for Facet/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from editorial.forms import (
    ImageAssetForm, LibraryImageAssociateForm, InternalImageForm, InternalImageLibraryAssociateForm,
    DocumentAssetForm, LibraryDocumentAssociateForm, InternalDocumentForm, InternalDocumentLibraryAssociateForm,
    AudioAssetForm, LibraryAudioAssociateForm, InternalAudioForm, InternalAudioLibraryAssociateForm,
    VideoAssetForm, LibraryVideoAssociateForm, InternalVideoForm, InternalVideoLibraryAssociateForm,
)

from editorial.models import (
    Project, Story, Item,
    ImageAsset, DocumentAsset, AudioAsset, VideoAsset,
    InternalImage, InternalDocument, InternalAudio, InternalVideo,
)


# Library Views

class AssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """Display media library of all assets."""

    template_name = 'editorial/assets/asset_list.html'

    def get_context_data(self):
        """Return all the (complex) assets associated entity or participant."""

        organization = self.request.user.organization
        tab = "Recent Assets"
        recentassets = organization.get_org_recent_media()
        return {'recentassets': recentassets, 'tab': tab,}


class ImageAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """Display media library of image assets."""

    template_name = 'editorial/assets/asset_list.html'

    def get_context_data(self):
        """Return all the (complex) assets associated with an organization."""

        tab = "Image Assets"
        organization = self.request.user.organization
        images = organization.get_org_image_library()
        return {'images': images, 'tab': tab,}


class DocumentAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """Display media library of document assets."""

    template_name = 'editorial/assets/asset_list.html'

    def get_context_data(self):
        """Return all the (complex) assets associated with an organization."""

        tab = "Document Assets"
        organization = self.request.user.organization
        documents = organization.get_org_document_library()
        return {'documents': documents, 'tab': tab,}


class AudioAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """Display media library of audio assets."""

    template_name = 'editorial/assets/asset_list.html'

    def get_context_data(self):
        """Return all the (complex) assets associated with an organization."""

        tab = "Audio Assets"
        organization = self.request.user.organization
        audio = organization.get_org_audio_library()
        return {'audio': audio, 'tab': tab,}


class VideoAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """ Display media library video assets."""

    template_name = 'editorial/assets/asset_list.html'

    def get_context_data(self):
        """Return all the (complex) assets associated with an organization."""

        tab = "Video Assets"
        organization = self.request.user.organization
        video = organization.get_org_video_library()
        return {'video': video, 'tab': tab,}


# Image Asset Views

class ImageAssetCreateView(LoginRequiredMixin, CreateView):
    """Upload an image to an item."""

    model = ImageAsset
    form_class = ImageAssetForm

    def form_valid(self, form):
        """Save -- but first add owner and organization to the image and
        add the image to the item.
        """

        self.object = image = form.save(commit=False)
        item_id = self.request.POST.get('item')
        item = get_object_or_404(Item, id=item_id)

        # set request based attributes
        image.participant_owner = self.request.user
        if item.entity_owner:
            image.entity_owner = item.entity_owner
        # FIXME how to approach images uploaded by a partner to an story/item owned
        # a partner organization
        image.save()
        # add image asset to item image_assets
        item.image_assets.add(image)
        item.save()

        return redirect('editorial:item_update', pk=item.id, story=item.story.id)


class LibraryImageAssociateView(LoginRequiredMixin, FormView):
    """ Add existing image(s) in the library to another item."""

    form_class = LibraryImageAssociateForm
    template_name = "editorial/assets/_library_image.html"

    def get_form_kwargs(self):
        """Pass some initial things to scaffold form."""
        kwargs = super(LibraryImageAssociateView, self).get_form_kwargs()
        kwargs['participant_owner'] = self.request.user
        if self.request.user.newsorganization:
            kwargs['entity_owner'] = self.request.user.newsorganization
        return kwargs

    def form_valid(self, form):
        """Handle submission of form."""

        item_id = self.kwargs['item']
        images = form.cleaned_data['images']
        item = get_object_or_404(Item, id=item_id)
        item.image_assets.add(*images)

        return redirect('item_edit', pk=item.id, story=item.story.id)


class ImageAssetDisassociateView(LoginRequiredMixin, View):
    """ Process form to remove an image from an item."""

    def post(self, request, item, image):
        """ Retrieve item and image from kwargs and remove image from item imageasset_set."""

        item_id = self.kwargs['item']
        image_id = self.kwargs['image']
        item = Facet.objects.get(id=item_id)
        image = ImageAsset.objects.get(id=image_id)
        item.image_assets.remove(image)

        return redirect('item_edit', pk=item.id, story=item.story.id)


class ImageAssetUpdateView(LoginRequiredMixin, UpdateView):
    """ Display editable detail information for a specific image asset."""

    model = ImageAsset
    form_class = ImageAssetForm
    template_name = 'editorial/assets/imageasset_form.html'

    def image_usage(self):
        """Get all facets an image is associated with."""
        return self.object.get_image_usage()

    def get_success_url(self):
        """Record edit activity."""

        return super(ImageAssetUpdateView, self).get_success_url()


class ImageAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """Handle deletion of an image asset.

    Assets can only be deleted from the library.
    """

    model = ImageAsset
    template_name = "editorial/assets/imageasset_delete.html"

    form_valid_message = "Deleted."
    form_invalid_message = "Please check form."

    def get_success_url(self):
        """Post deletion return to the media library."""

        return reverse('editorial:asset_library')


# Document Asset Views

class DocumentAssetCreateView(LoginRequiredMixin, CreateView):
    """Upload a document to an item."""

    model = DocumentAsset
    form_class = DocumentAssetForm

    def form_valid(self, form):
        """Save -- but first add owner and organization to the document and
        add the document to the item.
        """

        self.object = document = form.save(commit=False)
        item_id = self.request.POST.get('item')
        item = get_object_or_404(Item, id=item_id)

        # set request based attributes
        document.participant_owner = self.request.user
        if item.entity_owner:
            document.entity_owner = item.entity_owner
        # FIXME how to approach documents uploaded by a partner to an story/item owned
        # a partner organization
        document.save()
        # add document asset to item document_assets
        item.document_assets.add(document)
        item.save()

        return redirect('editorial:item_update', pk=item.id, story=item.story.id)


class LibraryDocumentAssociateView(LoginRequiredMixin, FormView):
    """ Add existing document(s) in the library to another item."""

    form_class = LibraryDocumentAssociateForm
    template_name = "editorial/assets/_library_document.html"

    def get_form_kwargs(self):
        """Pass some initial things to scaffold form."""
        kwargs = super(LibraryDocumentAssociateView, self).get_form_kwargs()
        kwargs['participant_owner'] = self.request.user
        if self.request.user.newsorganization:
            kwargs['entity_owner'] = self.request.user.newsorganization
        return kwargs

    def form_valid(self, form):
        """Handle submission of form."""

        item_id = self.kwargs['item']
        documents = form.cleaned_data['documents']
        item = get_object_or_404(Item, id=item_id)
        item.document_assets.add(*documents)

        return redirect('item_edit', pk=item.id, story=item.story.id)


class DocumentAssetDisassociateView(LoginRequiredMixin, View):
    """ Process form to remove a document from an item."""

    def post(self, request, item, document):
        """ Retrieve item and document from kwargs and remove document from item document_assets."""

        item_id = self.kwargs['item']
        doc_id = self.kwargs['document']
        item = Facet.objects.get(id=item_id)
        document = DocumentAsset.objects.get(id=doc_id)
        item.document_assets.remove(document)

        return redirect('item_edit', pk=item.id, story=item.story.id)


class DocumentAssetUpdateView(LoginRequiredMixin, UpdateView):
    """ Display editable detail information for a specific document asset."""

    model = DocumentAsset
    form_class = DocumentAssetForm
    template_name = 'editorial/assets/documentasset_form.html'

    def document_usage(self):
        """Get all facets a document is associated with."""
        return self.object.get_document_usage()

    def get_success_url(self):
        """Record edit activity."""

        return super(DocumentAssetUpdateView, self).get_success_url()


class DocumentAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """Handle deletion of a document asset.

    Assets can only be deleted from the library.
    """

    model = DocumentAsset
    template_name = "editorial/assets/documentasset_delete.html"

    form_valid_message = "Deleted."
    form_invalid_message = "Please check form."

    def get_success_url(self):
        """Post deletion return to the media library."""

        return reverse('editorial:asset_library')


# Audio Asset Views

class AudioAssetCreateView(LoginRequiredMixin, CreateView):
    """Upload audio to an item."""

    model = AudioAsset
    form_class = AudioAssetForm

    def form_valid(self, form):
        """Save -- but first add owner and organization to the audio and
        add the audio to the item.
        """

        self.object = audio = form.save(commit=False)
        item_id = self.request.POST.get('item')
        item = get_object_or_404(Item, id=item_id)

        # set request based attributes
        audio.participant_owner = self.request.user
        if item.entity_owner:
            audio.entity_owner = item.entity_owner
        # FIXME how to approach audios uploaded by a partner to an story/item owned
        # a partner organization
        audio.save()
        # add audio asset to item audio_assets
        item.audio_assets.add(audio)
        item.save()

        return redirect('editorial:item_update', pk=item.id, story=item.story.id)


class LibraryAudioAssociateView(LoginRequiredMixin, FormView):
    """ Add existing audio(s) in the library to another item."""

    form_class = LibraryAudioAssociateForm
    template_name = "editorial/assets/_library_audio.html"

    def get_form_kwargs(self):
        """Pass some initial things to scaffold form."""
        kwargs = super(LibraryAudioAssociateView, self).get_form_kwargs()
        kwargs['participant_owner'] = self.request.user
        if self.request.user.newsorganization:
            kwargs['entity_owner'] = self.request.user.newsorganization
        return kwargs

    def form_valid(self, form):
        """Handle submission of form."""

        item_id = self.kwargs['item']
        audio = form.cleaned_data['audio']
        item = get_object_or_404(Item, id=item_id)
        item.audio_assets.add(*audio)

        return redirect('item_edit', pk=item.id, story=item.story.id)


class AudioAssetDisassociateView(LoginRequiredMixin, View):
    """ Process form to remove an audio file from an item."""

    def post(self, request, item, audio):
        """ Retrieve item and audio from kwargs and remove audio from item audio_assets."""

        item_id = self.kwargs['item']
        audio_id = self.kwargs['audio']
        item = Facet.objects.get(id=item_id)
        audio = AudioAsset.objects.get(id=audio_id)
        item.audio_assets.remove(audio)

        return redirect('item_edit', pk=item.id, story=item.story.id)


class AudioAssetUpdateView(LoginRequiredMixin, UpdateView):
    """ Display editable detail information for a specific audio asset."""

    model = AudioAsset
    form_class = AudioAssetForm
    template_name = 'editorial/assets/audioasset_form.html'

    def audio_usage(self):
        """Get all facets a audio is associated with."""
        return self.object.get_audio_usage()

    def get_success_url(self):
        """Record edit activity."""

        return super(AudioAssetUpdateView, self).get_success_url()


class AudioAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """Handle deletion of an audio asset.

    Assets can only be deleted from the library.
    """

    model = AudioAsset
    template_name = "editorial/assets/audioasset_delete.html"

    form_valid_message = "Deleted."
    form_invalid_message = "Please check form."

    def get_success_url(self):
        """Post deletion return to the media library."""

        return reverse('editorial:asset_library')


# Video Asset Views

class VideoAssetCreateView(LoginRequiredMixin, CreateView):
    """Upload a video to an item."""

    model = VideoAsset
    form_class = VideoAssetForm

    def form_valid(self, form):
        """Save -- but first add owner and organization to the video and
        add the video to the item.
        """

        self.object = video = form.save(commit=False)
        item_id = self.request.POST.get('item')
        item = get_object_or_404(Item, id=item_id)

        # set request based attributes
        video.participant_owner = self.request.user
        if item.entity_owner:
            video.entity_owner = item.entity_owner
        # FIXME how to approach videos uploaded by a partner to an story/item
        # owned by a partner organization
        video.save()
        # add video asset to item video_assets
        item.video_assets.add(video)
        item.save()

        return redirect('editorial:item_update', pk=item.id, story=item.story.id)


class LibraryVideoAssociateView(LoginRequiredMixin, FormView):
    """ Add existing video(s) in the library to another item."""

    form_class = LibraryVideoAssociateForm
    template_name = "editorial/assets/_library_video.html"

    def get_form_kwargs(self):
        """Pass some initial things to scaffold form."""
        kwargs = super(LibraryVideoAssociateView, self).get_form_kwargs()
        kwargs['participant_owner'] = self.request.user
        if self.request.user.newsorganization:
            kwargs['entity_owner'] = self.request.user.newsorganization
        return kwargs

    def form_valid(self, form):
        """Handle submission of form."""

        item_id = self.kwargs['item']
        video = form.cleaned_data['video']
        item = get_object_or_404(Item, id=item_id)
        item.video_assets.add(*video)

        return redirect('item_edit', pk=item.id, story=item.story.id)


class VideoAssetDisassociateView(LoginRequiredMixin, View):
    """ Process form to remove a video file from an item."""

    def post(self, request, item, video):
        """ Retrieve item and video from kwargs and remove video from item video_assets."""

        item_id = self.kwargs['item']
        video_id = self.kwargs['video']
        item = Facet.objects.get(id=item_id)
        video = VideoAsset.objects.get(id=video_id)
        item.video_assets.remove(video)

        return redirect('item_edit', pk=item.id, story=item.story.id)


class VideoAssetUpdateView(LoginRequiredMixin, UpdateView):
    """ Display editable detail information for a specific video asset."""

    model = VideoAsset
    form_class = VideoAssetForm
    template_name = 'editorial/assets/videoasset_form.html'

    def video_usage(self):
        """Get all facets an video is associated with."""
        return self.object.get_video_usage()

    def get_success_url(self):
        """Record edit activity."""

        return super(VideoAssetUpdateView, self).get_success_url()


class VideoAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """Handle deletion of a video asset.

    Assets can only be deleted from the library.
    """

    model = VideoAsset
    template_name = "editorial/assets/videoasset_delete.html"

    form_valid_message = "Deleted."
    form_invalid_message = "Please check form."

    def get_success_url(self):
        """Post deletion return to the media library."""

        return reverse('editorial:asset_library')


# Simple Asset Library Views

# ACCESS: Only an org's users should be able to see an organization's internal asset library
class SimpleAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class InternalImageAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class InternalDocumentAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class InternalAudioAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class InternalVideoAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass

# Simple Image

# ACCESS: Any org user, or user from an organization that is in collaborate_with
# should be able to create a internal asset for P, Sr, St, F
# Contractors should only be able to do so for PSSF that they have access to
# That should be handled by limiting which PSSF they have access to.
class InternalImageCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


# ACCESS: Any org user should be able to add an asset for a P, Sr, St, F
# A user from an organization that is in collaborate_with or
# contractors should not be able to do this because doing so requires access to
# an org's entire asset library.
class InternalImageLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class InternalImageUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class InternalImageAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


class InternalImageAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass


# Simple Document
class InternalDocumentCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class InternalDocumentUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class InternalDocumentAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


# ACCESS: Any org user should be able to add an asset for a P, Sr, St, F
# A user from an organization that is in collaborate_with or
# contractors should not be able to do this because doing so requires access to
# an org's entire asset library.
class InternalDocumentLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class InternalDocumentAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass


# Simple Audio
class InternalAudioCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class InternalAudioUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class InternalAudioAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


# ACCESS: Any org user should be able to add an asset for a P, Sr, St, F
# A user from an organization that is in collaborate_with or
# contractors should not be able to do this because doing so requires access to
# an org's entire asset library.
class InternalAudioLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class InternalAudioAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass


# Simple Video
class InternalVideoCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class InternalVideoUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class InternalVideoAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


# ACCESS: Any org user should be able to add an asset for a P, Sr, St, F
# A user from an organization that is in collaborate_with or
# contractors should not be able to do this because doing so requires access to
# an org's entire asset library.
class InternalVideoLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class InternalVideoAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass

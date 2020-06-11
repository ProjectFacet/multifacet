"""Pickup Views for Item/Pickup.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from pickup.forms import ()

from pickup.models import ()


#FIXME Refinement for a partner to be able to go back and pick up additional or new Items/Components
class PickupStoryView(LoginRequiredMixin, View):
    """Pickup a story and related items.

    A user should be able to click and pickup a partner story
    this should make a pickup of the story for the new organization
    it should come with all associated assets - image, doc, audio, video
    it should not come with events, notes, tasks, or internal assets
    After a user has copied a story, there should be a visual cue in the interface
    or a js alert (something) that notifies a user should they try to pickup a
    story that another user from their org has already copied that specific story.

    Phases of Functionality:
    1. A user can pickup a story from a sharing partner. This accomplished what's
    listed above.
    2. A user should be able to select the specific items of a story they
    want to pickup. (Doesn't need to be more granular than that, they don't need to
    select images like in download)
    3. A story that's been updated since it was marked ready_to_share has a visual cue
    that it has been updated. Users who have already copied it, should get some sort
    of notification that updates are available. This is important in the case of
    corrections.

    """

    def post(self, request, story):
        print "In post"
        story = self.kwargs['story']
        original_story = get_object_or_404(Story, id=story)
        original_org = original_story.organization
        original_items = original_story.item_set.all()

        user = self.request.user
        organization = self.request.user.organization
        partner = self.request.user.organization

        print "stuff is happening"
        # Create a pickup of the story and a storypickupdetail record
        copied_story = Story.pickup_story(original_story)
        copied_story.owner = user
        copied_story.organization = organization
        copied_story.save()
        story_pickup_record = StoryPickupDetail.objects.create_story_pickup_record(
            original_org=original_org,
            partner=partner,
            original_story=original_story,
            partner_story=copied_story
            )

        # Create pickup of items if they exist
        # Pickup the Item
        if original_items:
            # get item templates and make copies if org is not null
            print "if original items"
            for item in original_items:

                # pickup the editor and credit (m2m's) so we can add on pickup
                editor = item.editor.all()
                credit = item.credit.all()

                copied_item = item.pickup()

                copied_item.editor = editor
                copied_item.credit = credit

                print "Copied Item exists"
                print "CF: ", copied_item
                copied_item.story = copied_story
                print "CFS"
                copied_item.owner = user
                print "CFO"
                copied_item.organization = organization
                print "CFOR"
                copied_item.save()
                print "CF Saved"
                item_pickup_record = ItemPickupDetail.objects.create_item_pickup_record(
                    original_org=original_org,
                    partner=partner,
                    original_item=item,
                    partner_item=copied_item
                )
                print "item pickup record"


            # create pickup of item images
            original_item_images = original_story.get_story_images()
            print "original item images"
            for image in original_item_images:
                copied_image = image.pickup()
                copied_image.owner = user
                copied_image.organization = organization
                copied_image.save()
                imageasset_pickup_record = ImageAssetPickupDetail.objects.create_imageasset_pickup_record(
                    original_org=original_org,
                    partner=partner,
                    original_imageasset=image,
                    partner_imageasset=copied_image
                )
                # add image to copied item
                copied_item.image_assets.add(copied_image)
                copied_item.save()

            # create pickup of item documents
            original_item_documents = original_story.get_story_documents()
            print "original item documents"
            for document in original_item_documents:
                copied_document = document.pickup()
                copied_document.owner = user
                copied_document.organization = organization
                copied_document.save()
                documentasset_pickup_record = DocumentAssetPickupDetail.objects.create_documentasset_pickup_record(
                    original_org=original_org,
                    partner=partner,
                    original_documentasset=document,
                    partner_documentasset=copied_document
                )
                # add document to copied item
                copied_item.document_assets.add(copied_document)
                copied_item.save()


            # create pickup of item audio
            original_item_audiofiles = original_story.get_story_audio()
            print "original item audio"
            for audio in original_item_audiofiles:
                copied_audio = audio.pickup()
                copied_audio.owner = user
                copied_audio.organization = organization
                copied_audio.save()
                audioasset_pickup_record = AudioAssetPickupDetail.objects.create_audioasset_pickup_record(
                    original_org=original_org,
                    partner=partner,
                    original_audioasset=audio,
                    partner_audioasset=copied_audio
                )
                # add audio to copied item
                copied_item.audio_assets.add(copied_audio)
                copied_item.save()

            # create pickup of item video
            original_item_videos = original_story.get_story_video()
            print "original item video"
            for video in original_item_videos:
                copied_video = video.pickup()
                copied_video.owner = user
                copied_video.organization = organization
                copied_video.save()
                videoasset_pickup_record = VideoAssetPickupDetail.objects.create_videoasset_pickup_record(
                    original_org=original_org,
                    partner=partner,
                    original_videoasset=video,
                    partner_videoasset=copied_video
                )
                # add video to copied item
                copied_item.video_assets.add(copied_video)
                copied_item.save()

        # record action for activity story_team
        # action.send(self.request.user, verb="picked up", action_object=original_story)

        return redirect('network_stories')

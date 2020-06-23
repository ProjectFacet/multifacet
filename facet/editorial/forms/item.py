"""Forms for Items and related entities."""

# from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.db.models import Q
from django.forms import Textarea, TextInput, Select, CheckboxInput, CheckboxSelectMultiple
from django.contrib.postgres.forms import SimpleArrayField
# from tinymce.widgets import TinyMCE

from facet.widgets import (
    ArrayFieldSelectMultiple,
    _TextInput,
    _Textarea,
    _Select,
)

from editorial.models import (
    Story,
    Item,
    ItemTemplate,
    ContentLicense,
)

from editorial.models.item_template import COMMON_FIELDS


class ItemTemplateForm(forms.ModelForm):
    """Form for editing item templates."""

    def clean_fields_used(self):
        """There may be spaces around entries; strip these off."""

        return [f.strip() for f in self.cleaned_data['fields_used']]

    class Meta:
        model = ItemTemplate
        fields = "__all__"
        widgets = {
            'name': TextInput(
                attrs={'class': 'form_control', 'id': 'item_name', 'id':'item_name', 'rows': 2, 'placeholder': 'Name'}),
            'description': Textarea(
                attrs={'class': 'md-textarea form_control', 'id': 'item_description', 'id':'item_description', 'rows': 3, 'placeholder': 'Description'}),
            'is_active': CheckboxInput(
                attrs={'class': 'form-check-input', 'id':'item_active',}),
        }


def get_item_form_for_template(template_id):
    """Return custom item form.

    The form for an item depends upon the template for that item, rather than always
    being a particular set of fields. Therefore, this function generates a dynamic class
    with the correct fields for the item.
    """

    extra_fields = ItemTemplate.objects.get(id=template_id).fields_used

    class ItemForm(forms.ModelForm):
        """Form for an item. Dynamically selects fields based on template."""

        def __init__(self, *args, **kwargs):
            story = kwargs.pop('story', None)
            template = kwargs.pop('template', None)
            entity_owner = kwargs.pop('entity_owner', None)
            participant_owner = kwargs.pop('participant_owner', None)

            super(ItemForm, self).__init__(*args, **kwargs)

            if story:
                self.instance.story = story
            if template:
                self.instance.template = template
            if entity_owner:
                self.instance.entity_owner = entity_owner
            if participant_owner:
                self.instance.participant_owner = participant_owner

            # limit to team_vocab

            story = self.instance.story
            story_team_vocab = Story.get_team_vocab(story)
            print("STORY: ", story)
            print("STV: ", story_team_vocab)

            # when stories are copied; editors and creditees should remain as
            # possibilities in the drop-down menu
            if self.instance.id:
                self.fields['credit'].queryset = (story_team_vocab | self.instance.credit.all()).distinct()
                self.fields['editor'].queryset = (story_team_vocab | self.instance.editor.all()).distinct()
            else:
                self.fields['credit'].queryset = story_team_vocab
                self.fields['editor'].queryset = story_team_vocab

            # We want to handle cases where templates are made inactive, or
            # when an item is copied to an entity_owner other than the one
            # that has the matching templateself.
            #
            # So: the list of possible templates for this item is both:
            # - the current templates
            # - templates for this entity_owner
            self.fields['template'].queryset = (
                ItemTemplate.objects.filter(id=self.instance.template_id)
                | self.instance.entity_owner.get_item_templates())

            if 'content_license' in self.fields:
                self.fields['content_license'].queryset = ContentLicense.objects.filter(
                    Q(entity_owner=story.entity_owner) | Q(entity_owner__isnull=True))
                self.fields['content_license'].empty_label = 'Select a license'

            if 'producer' in self.fields:
                self.fields['producer'].queryset = story_team_vocab
                self.fields['producer'].empty_label = 'Select a producer'

        # due_edit = forms.DateTimeField(
        #     required=False,
        #     widget=DateTimePicker(
        #         options={'format': 'YYYY-MM-DD HH:mm'},
        #         attrs={'id': 'dueedit_picker'}
        #     )
        # )
        #
        # run_date = forms.DateTimeField(
        #     required=False,
        #     widget=DateTimePicker(
        #         options={'format': 'YYYY-MM-DD HH:mm'},
        #         attrs={'id': 'rundate_picker'}
        #     )
        # )
        #
        # tape_datetime = forms.DateTimeField(
        #     required=False,
        #     widget=DateTimePicker(
        #         options={'format': 'YYYY-MM-DD HH:mm'},
        #         attrs={'id': 'tapedate_picker'}
        #     )
        # )

        # content = forms.CharField(widget=TinyMCE(attrs={'rows': 20}))

        class Meta:
            model = Item

            fields = list(COMMON_FIELDS) + ['template'] + extra_fields

            widgets = {
                'name': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_name', 'rows': 2, 'placeholder': 'Name'}),
                'headline': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_headline', 'rows': 2, 'placeholder': 'Headline'}),
                'description': Textarea(
                    attrs={'class': 'md-textarea form_control', 'id': 'item_description', 'rows': 3, 'placeholder': 'Description'}),
                'content': Textarea(
                        attrs={'class': 'md-textarea form_control', 'id': 'item_content', 'rows': 10, 'placeholder': 'Content'}),
                'editor': ArrayFieldSelectMultiple(
                    attrs={'class': 'chosen-select mdb-select md-form', 'id': 'item-editor', 'data-placeholder': 'Select Editing Team'}),
                'credit': ArrayFieldSelectMultiple(
                    attrs={'class': 'chosen-select mdb-select md-form', 'id': 'item-credit', 'data-placeholder': 'Select Credited Team'}),
                'status': Select(
                    attrs={'class': 'form_control', 'id': 'item_status',}),
                'keywords': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_keywords', 'placeholder': 'Keywords'}),
                # template field
                'template': Select(
                    attrs={'class': 'form_control', 'id': 'item_template',}),
                # Optional Fields
                'excerpt': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_excerpt', 'rows': 2, 'placeholder': 'Excerpt'}),
                'update_note': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_update', 'rows': 2, 'placeholder': 'Updates to this item.'}),
                'share_note': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_share', 'rows': 2, 'placeholder': 'Notes for sharing this item.'}),
                'edit_note': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_edit', 'rows': 2, 'placeholder': 'Notes on editing this item'}),
                'dateline': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_dateline', 'rows': 2, 'placeholder': 'Dateline'}),
                'topic_code': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_topic', 'rows': 2, 'placeholder': 'Topic'}),
                'internal_code': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_internal', 'rows': 2, 'placeholder': 'Internal code'}),
                'length': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_length', 'rows': 2, 'placeholder': 'Length (time)'}),
                'wordcount': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_wordcount', 'rows': 2, 'placeholder': 'Wordcount'}),
                'content_license': Select(
                    attrs={'class': 'form_control', 'id': 'item_content_license',}),
                'related_links': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_related_links', 'rows': 2, 'placeholder': 'Related links (urls)'}),
                'github_link': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_github', 'rows': 2, 'placeholder': 'Github Link'}),
                'sources': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_sources', 'rows': 2, 'placeholder': 'Sources in this story'}),
                'pronounciations': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_pronounciations', 'rows': 2, 'placeholder': 'Pronounciations'}),
                'sponsors': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_sponsors', 'rows': 2, 'placeholder': 'Sponsors'}),
                'pull_quotes': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_pull_quotes', 'rows': 2, 'placeholder': 'Pull quotes'}),
                'embeds': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_embeds', 'rows': 2, 'placeholder': 'Embeds (html)'}),
                'sidebar_content': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_sidebar', 'rows': 2, 'placeholder': 'Sidebar content'}),
                'producer': Select(
                    attrs={'class': 'form_control', 'id': 'item_producer',}),
                'series_title': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_series_title', 'rows': 2, 'placeholder': 'Series Title'}),
                'episode_number': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_episode_number', 'rows': 2, 'placeholder': 'Episode Number'}),
                'usage_rights': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_usage_rights', 'rows': 2, 'placeholder': 'Usage Rights'}),
                'locations': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_locations', 'rows': 2, 'placeholder': 'Filming Locations'}),
                'custom_one': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_custom_one', 'rows': 2, 'placeholder': 'Custom Info One'}),
                'custom_two': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_custom_two', 'rows': 2, 'placeholder': 'Custom Info Two'}),
                'custom_three': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_custom_three', 'rows': 2, 'placeholder': 'Custom Info Three'}),
                'custom_four': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_custom_four', 'rows': 2, 'placeholder': 'Custom Info Four'}),
                'custom_five': TextInput(
                    attrs={'class': 'form_control', 'id': 'item_custom_five', 'rows': 2, 'placeholder': 'Custom Info Five'}),
            }

        def get_fields_to_show(self):
            """Returns list of extra fields, to display on form."""

            return [self[f] for f in extra_fields]

    return ItemForm


class ItemPreCreateForm(forms.Form):
    """Form to "pre-create" an item; used to create correct Item form.

    The job of this form is just to gather the name of the item and the template; it is
    used by a view that then uses these two fields to prepopulate the real item creation
    form.
    """

    def __init__(self, *args, **kwargs):
        entity_owner = kwargs.pop('entity_owner', None)
        participant_owner = kwargs.pop('participant_owner', None)
        super(ItemPreCreateForm, self).__init__(*args, **kwargs)
        # Expand filter to accomodate network partners creating an item on a collaborative story
        if entity_owner:
            self.fields['template'].queryset = entity_owner.get_item_templates()
        elif participant_owner:
            self.fields['template'].queryset = participant_owner.get_item_templates()
        else:
            self.fields['template'].empty_label = "Select a template"

    name = forms.CharField(
        label="Item Name",
    )

    template = forms.ModelChoiceField(
        ItemTemplate.objects.all(),
    )

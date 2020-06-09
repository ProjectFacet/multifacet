"""Item Template Views for Item/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from editorial.forms import (
    ItemTemplateForm,
    ItemPreCreateForm,
    get_item_form_for_template,
)

from editorial.models import (
    Story,
    Item,
    ItemTemplate,
    ImageAsset,
    DocumentAsset,
    AudioAsset,
    VideoAsset,
)


class ItemTemplateCreateView(LoginRequiredMixin, CreateView):
    """Create an item template."""

    model = ItemTemplate
    form_class = ItemTemplateForm

    template_name = 'item/item_template_form.html'


    form_invalid_message = "Something went wrong."
    form_valid_message = "Template created."

    def form_valid(self, form):
        """Save -- but first adding owner and organization."""

        self.object = template = form.save(commit=False)

        form_fields = self.request.POST.getlist('fields')

        template.owner = self.request.user
        template.organization = self.request.user.organization
        template.fields_used = form_fields

        template.save()
        form.save_m2m()

        action.send(self.request.user, verb="created", action_object=self.object)

        return redirect(self.get_success_url())


class ItemTemplateUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """Edit an item template."""

    model = ItemTemplate
    form_class = ItemTemplateForm

    template_name = 'item/item_template_form.html'

    form_invalid_message = "Something went wrong."
    form_valid_message = "Changes saved."

    def get_object(self):
        itemtemplate = ItemTemplate.objects.get(pk=self.kwargs['template'])
        return itemtemplate

    def form_valid(self, form):
        """Handle submission of form manually."""

        org = Organization.objects.get(pk=self.kwargs['org'])
        # Retrieve form values manually
        ft_id = self.request.POST.get('itemtemplate')
        form_fields = self.request.POST.getlist('fields')
        name = self.request.POST.get('name')
        description = self.request.POST.get('description')
        is_active = form.cleaned_data['is_active']

        # Set new values
        itemtemplate = ItemTemplate.objects.get(id=ft_id)
        itemtemplate.name = name
        itemtemplate.description = description
        itemtemplate.is_active = is_active
        itemtemplate.fields_used = form_fields
        itemtemplate.save()

        action.send(self.request.user, verb="edited", action_object=self.object)

        return redirect('item_template_list', org=org.id)


class ItemTemplateListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """List all sitewide and organization item templates. Distinguishes between
    active and not active templates.
    """

    context_object_name = 'itemtemplates'
    template_name = 'item/item_template_list.html'

    def get_context_data(self, **kwargs):
        """Group itemtemplates for display."""

        context = super(ItemTemplateListView, self).get_context_data(**kwargs)
        org = Organization.objects.get(pk=self.kwargs['org'])
        basetemplates = ItemTemplate.objects.filter(organization_id__isnull=True)
        activetemplates = ItemTemplate.objects.filter(Q(organization_id=org) & Q(is_active=True))
        inactivetemplates = ItemTemplate.objects.filter(Q(organization_id=org) & Q(is_active=False))
        context['basetemplates'] = basetemplates
        context['activetemplates'] = activetemplates
        context['inactivetemplates'] = inactivetemplates
        return context


class ItemTemplateDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """Used to display details about sitewide tempates that are not editable by users.

    For editable templates, the users are sent directly to the edit form for details.
    """

    model = ItemTemplate
    template_name = 'item/item_template_detail.html'

    def get_object(self):
        return ItemTemplate.objects.get(pk=self.kwargs['template'])


class ItemTemplateDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """View for handling deletion of an item template.

    In this project, we expect deletion to be done via a JS pop-up UI; we don't expect to
    actually use the "do you want to delete this?" Django-generated page. However, this is
    available if useful.
    """

    #FIXME troubleshoot delete js
    model = ItemTemplate
    template_name = "item/item_template_delete.html"

    form_valid_message = "Deleted."
    form_invalid_message = "Please check form."

    def get_object(self):
        return ItemTemplate.objects.get(pk=self.kwargs['template'])

    def get_success_url(self):
        """Post-deletion, return to the template list."""

        return reverse('item_template_list',kwargs={'org':self.request.user.organization.id})

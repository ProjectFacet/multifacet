"""Invoice Views for Facet/Freelance.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from freelance.forms import (
    FreelanceInvoiceForm
)

from freelance.models import (
    FreelanceInvoice,
)

from participant.models import (
    FreelanceJournalist,
    FreelanceManager,
)


class FreelanceInvoiceListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """Show a freelancer their invoices."""

    model = FreelanceInvoice

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fj_id = self.kwargs['fj']
        freelancejournalist = FreelanceJournalist.objects.get(id=fj_id)
        context['invoices'] = freelancejournalist.freelance_invoice_set.all()
        return context


class OrganizationInvoiceListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """Show a freelance manager of an organization, the invoices of the organization."""

    model = FreelanceInvoice

    def test_user(self, user):
        """User must be affiliated with this news organization to view the dashboard."""

        org_id = self.kwargs['org']
        newsorganization = NewsOrganization.objects.get(id=org_id)
        if user.freelance_manager.newsorganization == newsorganization:
            return True

        raise PermissionDenied()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fj_id = self.kwargs['fj']
        freelancejournalist = FreelanceJournalist.objects.get(id=fj_id)
        context['invoices'] = freelancejournalist.freelance_invoice_set.all()
        return context


class InvoiceCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """Create a new invoice."""

    model = FreelanceInvoice
    form_class = FreelanceInvoiceForm
    template_name = 'freelance_invoice/freelance_invoice_form.html'

    form_invalid_message = "Something went wrong."
    form_valid_message = "Invoice created."


class InvoiceUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """Update an invoice."""

    model = FreelanceInvoice
    form_class = FreelanceInvoiceForm
    template_name = 'freelance_invoice/freelance_invoice_form.html'

    form_invalid_message = "Something went wrong."
    form_valid_message = "Invoice updated."


class InvoiceDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """View an invoice's detail."""

    model = FreelanceInvoice
    template_name = 'freelance_invoice/freelance_invoice_detail.html'

    def internal_images(self):
        """Return internal images."""
        pass

    def internal_documents(self):
        """Return internal documents."""
        pass


class InvoiceDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """Delete an invoice."""
    pass

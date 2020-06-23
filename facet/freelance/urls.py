from django.urls import path

from .views import (
    journalist_freelance_dashboard,
    journalist_freelance,
    freelance_manager,
    affiliation,
    freelance_invoice,
    call,
    pitch,
    assignment,

)


app_name = 'freelance'
urlpatterns = [
    path('dashboard/', journalist_freelance_dashboard.FreelanceJournalistDashboardView.as_view(), name='dashboard_freelance'),
    path('profile/create/', journalist_freelance.FreelanceJournalistCreateView.as_view(), name='freelance_journalist_create'),
    path('profile/<pk>/', journalist_freelance.FreelanceJournalistDetailView.as_view(), name='freelance_journalist_detail'),
    path('profile/<pk>/public/', journalist_freelance.FreelanceJournalistPublicProfileDetailView.as_view(), name='freelance_journalist_public_profile'),
    path('profile/<pk>/update/', journalist_freelance.FreelanceJournalistProfileUpdateView.as_view(), name='freelance_journalist_update'),
    path('profile/<pk>/delete/', journalist_freelance.FreelanceJournalistDeleteView.as_view(), name='freelance_journalist_delete'),
    # manager
    path('manager/create/', freelance_manager.FreelanceManagerCreateView.as_view(), name='freelance_manager_create'),
    path('manager/<pk>/', freelance_manager.FreelanceManagerDashboardView.as_view(), name='freelance_manager_dashboard'),
    path('manager/<pk>/public/', freelance_manager.FreelanceManagerPublicProfileDetailView.as_view(), name='freelance_manager__public_profile'),
    path('manager/<pk>/update/', freelance_manager.FreelanceManagerUpdateView.as_view(), name='freelance_manager_update'),
    path('manager/<pk>/delete/', freelance_manager.FreelanceManagerDeleteView.as_view(), name='freelance_manager_delete'),
    # freelancer affiliation record
    path('organization/<org>/freelance/<fj>/affilitation/create/', affiliation.FreelancerAffiliationRecordCreateView.as_view(), name='freelance_affiliation_record_create'),
    path('organization/<org>/freelance/<fj>/affilitation/<pk>/', affiliation.FreelancerAffiliationRecordDetailView.as_view(), name='freelance_affiliation_record_detail'),
    path('organization/<org>/freelance/<fj>/affilitation/<pk>/update/', affiliation.FreelancerAffiliationRecordUpdateView.as_view(), name='freelance_affiliation_record_update'),
    path('organization/<org>/freelance/<fj>/affilitation/<pk>/delete/', affiliation.FreelancerAffiliationRecordDeleteView.as_view(), name='freelance_affiliation_record_delete'),
    # organization affilitation record
    path('<fj>/organization/<org>/affilitation/create/', affiliation.OrganizationAffiliationRecordCreateView.as_view(), name='organization_affiliation_record_create'),
    path('<fj>/organization/<org>/affilitation/<pk>/', affiliation.OrganizationAffiliationRecordDetailView.as_view(), name='organization_affiliation_record_detail'),
    path('<fj>/organization/<org>/affilitation/<pk>/update/', affiliation.OrganizationAffiliationRecordUpdateView.as_view(), name='organization_affiliation_record_update'),
    path('<fj>/organization/<org>/affilitation/<pk>/delete/', affiliation.OrganizationAffiliationRecordDeleteView.as_view(), name='organization_affiliation_record_delete'),
    # invoice
    path('<fj>/invoices', freelance_invoice.FreelanceInvoiceListView.as_view(), name='freelance_invoice_list'),
    path('<org>/invoices', freelance_invoice.OrganizationInvoiceListView.as_view(), name='organization_invoice_list'),
    path('<fj>/create/', freelance_invoice.InvoiceCreateView.as_view(), name='freelance_invoice_create'),
    path('<fj>/invoice/<pk>/', freelance_invoice.InvoiceDetailView.as_view(), name='freelance_invoice_detail'),
    path('<fj>/invoice/<pk>/update/', freelance_invoice.InvoiceUpdateView.as_view(), name='freelance_invoice_update'),
    path('<fj>/invoice/<pk>/delete/', freelance_invoice.InvoiceDeleteView.as_view(), name='freelance_invoice_delete'),
    # call
    path('public/calls/', call.FreelanceCallListView.as_view(), name='public_call_list'),
    path('<org>/calls/', call.OrganizationCallListView.as_view(), name='organization_call_list'),
    path('call/create/', call.CallCreateView.as_view(), name='call_create'),
    path('call/<pk>/', call.CallDetailView.as_view(), name='call_detail'),
    path('call/<pk>/update/', call.CallUpdateView.as_view(), name='call_update'),
    path('call/<pk>/delete/', call.CallDeleteView.as_view(), name='call_delete'),
    # pitch
    path('<fj>/pitches/', pitch.FreelancePitchListView.as_view(), name='freelance_pitch_list'),
    path('<org>/pitches/', pitch.OrganizationPitchListView.as_view(), name='organization_pitch_list'),
    path('pitch/create/', pitch.PitchCreateView.as_view(), name='pitch_create'),
    path('pitch/<pk>/', pitch.PitchDetailView.as_view(), name='pitch_detail'),
    path('pitch/<pk>/update/', pitch.PitchUpdateView.as_view(), name='pitch_update'),
    path('pitch/<pk>/delete/', pitch.PitchDeleteView.as_view(), name='pitch_delete'),
    # assignment
    path('<fj>/assignments/', assignment.FreelanceAssignmentListView.as_view(), name='freelance_assignment_list'),
    path('<org>/assignments/', assignment.OrganizationAssignmentListView.as_view(), name='assignment_list'),
    path('assignment/create/', assignment.AssignmentCreateView.as_view(), name='assignment_create'),
    path('assignment/<pk>/', assignment.AssignmentDetailView.as_view(), name='assignment_detail'),
    path('assignment/<pk>/update/', assignment.AssignmentUpdateView.as_view(), name='assignment_update'),
    path('assignment/<pk>/delete/', assignment.AssignmentDeleteView.as_view(), name='assignment_delete'),
]

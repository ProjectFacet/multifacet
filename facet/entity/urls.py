from django.urls import path

from .views import (
    organization_news,
    network_newsorganization,
)

app_name = 'entity'
urlpatterns = [
    # News Organization
    path('organization/news/new/', organization_news.NewsOrganizationCreateView.as_view(), name='organization_news_new'),
    path('organization/news/<pk>/', organization_news.NewsOrganizationDetailView.as_view(), name='organization_news_detail'),
    path('organization/news/<pk>/update/', organization_news.NewsOrganizationUpdateView.as_view(), name='organization_news_update'),
    path('organization/news/<pk>/delete/', organization_news.NewsOrganizationDeleteView.as_view(), name='organization_news_delete'),

    # News Organization Network
    path('network/newsorganization/new/', network_newsorganization.NewsOrganizationNetworkCreateView.as_view(), name='network_newsorganization_new'),
    path('network/newsorganization/<pk>/', network_newsorganization.NewsOrganizationNetworkDetailView.as_view(), name='network_newsorganization_detail'),
    path('network/newsorganization/<pk>/update/', network_newsorganization.NewsOrganizationNetworkUpdateView.as_view(), name='network_newsorganization_update'),
    path('network/newsorganization/<pk>/delete/', network_newsorganization.NewsOrganizationNetworkDeleteView.as_view(), name='network_newsorganization_delete'),
    path('network/newsorganization/<pk>/list/', network_newsorganization.NewsOrganizationNetworkListView.as_view(), name='network_newsorganization_list'),
    path('network/newsorganization/stories/', network_newsorganization.NewsOrganizationNetworkStoryListView.as_view(), name='network_newsorganization_stories'),
    path('network/newsorganization/<pk>/invitation/', network_newsorganization.NewsOrganizationNetworkInvitationOfferView.as_view(), name='network_newsorganization_invitation'),
    path('network/newsorganization/<pk>/invitation/response/', network_newsorganization.NewsOrganizationNetworkInvitationResponseView.as_view(), name='network_newsorganization_invitation_response'),
    path('network/newsorganization/<pk>/joinrequest/', network_newsorganization.NewsOrganizationNetworkJoinRequestView.as_view(), name='network_newsorganization_joinrequest'),
    path('network/newsorganization/<pk>/joinrequest/response/', network_newsorganization.NewsOrganizationNetworkJoinResponseView.as_view(), name='network_newsorganization_invitation_joinrequest_response'),
]

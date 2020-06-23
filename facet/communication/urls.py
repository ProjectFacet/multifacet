from django.urls import path

from .views import (
    discussion,
    directmessage,
)


app_name = 'communication'
urlpatterns = [
    # Discussion / Comment
    path('discussion/create', discussion.DiscussionCreateView.as_view(), name='discussion_channel_new'),
    path('discussion/<pk>/channel/update', discussion.DiscussionUpdateView.as_view(), name='discussion_channel_update'),
    path('discussion/<pk>/delete', discussion.DiscussionDeleteView.as_view(), name='discussion_delete'),
    path('discussion/<pk>/comment/create', discussion.CommentCreateView.as_view(), name='comment_create'),
    path('discussion/<discussion>/comment/<pk>/update', discussion.CommentCreateView.as_view(), name='comment_update'),
    path('discussion/<discussion>/comment/<pk>/delete', discussion.CommentDeleteView.as_view(), name='comment_delete'),
    # Direct Message
    path('directmessage/exchange/create', directmessage.DirectMessageExchangeCreateView.as_view(), name='directmessage_exchange_new'),
    path('directmessage/exchange/<pk>/dm/create', directmessage.DirectMessageCreateView.as_view(), name='directmessage_new'),
    path('directmessage/exchange/<exchange>/dm/<pk>/update', directmessage.DirectMessageUpdateView.as_view(), name='directmessage_update'),
    path('directmessage/exchange/<exchange>/dm/<pk>/delete', directmessage.DirectMessageDeleteView.as_view(), name='directmessage_delete'),
]

from django.urls import path

from .views import (
    project,
    story,
    item,
    item_template,
    asset,
)

app_name = 'editorial'
urlpatterns = [
    #Project
    path('project/new/', project.ProjectCreateView.as_view(), name='project_new'),
    path('project/<pk>/', project.ProjectDetailView.as_view(), name='project_detail'),
    path('project/<pk>/update/', project.ProjectUpdateView.as_view(), name='project_update'),
    path('project/<pk>/delete/', project.ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<pk>/team/update/', project.ProjectTeamUpdateView.as_view(), name='project_team_update'),
    path('project/<pk>/stories/', project.ProjectStoryView.as_view(), name='project_stories'),
    path('project/<pk>/assets/', project.ProjectAssetView.as_view(), name='project_assets'),
    path('project/<pk>/tasks/', project.ProjectTaskView.as_view(), name='project_tasks'),
    path('project/<pk>/notes/', project.ProjectNoteView.as_view(), name='project_notes'),
    # path('/project/<pk>/note/(?P<note>\d+)/content$', notes.NoteContent.as_view(), name='note_content'),
    path('project/<pk>/calendar/', project.ProjectScheduleView.as_view(), name='project_schedule'),
    # Project lists
    path('project/list/', project.ProjectListRedirectView.as_view(), name='project_list'),
    path('<pk>/project/list/', project.StaffJournalistProjectListView.as_view(), name='staff_project_list'),
    path('<pk>/project/list/', project.UnaffiliatedStaffJournalistProjectListView.as_view(), name='unaffiliated_project_list'),
    path('<pk>/project/list/', project.FreelanceJournalistProjectListView.as_view(), name='freelance_project_list'),
    path('<pk>/project/list/', project.NewsOrganizationProjectListView.as_view(), name='newsorganization_project_list'),
    path('<pk>/project/list/', project.NewsOrganizationNetworkProjectListView.as_view(), name='newsnetwork_project_list'),
    # Story
    path('story/new/', story.StoryCreateView.as_view(), name='story_new'),
    path('story/<pk>/', story.StoryDetailView.as_view(), name='story_detail'),
    path('story/<pk>/update/', story.StoryUpdateView.as_view(), name='story_update'),
    path('story/<pk>/delete/', story.StoryDeleteView.as_view(), name='story_delete'),
    path('story/<pk>/team/update/', story.StoryTeamUpdateView.as_view(), name='story_team_update'),
    path('story/<pk>/items/', story.StoryItemView.as_view(), name='story_items'),
    path('story/<pk>/assets/', story.StoryAssetView.as_view(), name='story_assets'),
    path('story/<pk>/tasks/', story.StoryTaskView.as_view(), name='story_tasks'),
    path('story/<pk>/notes/', story.StoryNoteView.as_view(), name='story_notes'),
    # path('/story/<pk>/note/(?P<note>\d+)/content$', notes.NoteContent.as_view(), name='note_content'),
    path('story/<pk>/calendar/', story.StoryScheduleView.as_view(), name='story_schedule'),
    # Story lists
    path('story/list/', story.StoryListRedirectView.as_view(), name='story_list'),
    path('<pk>/story/list/', story.StaffJournalistStoryListView.as_view(), name='staff_story_list'),
    path('<pk>/story/list/', story.UnaffiliatedStaffJournalistStoryListView.as_view(), name='unaffiliated_story_list'),
    path('<pk>/story/list/', story.FreelanceJournalistStoryListView.as_view(), name='freelance_story_list'),
    path('<pk>/story/list/', story.NewsOrganizationStoryListView.as_view(), name='newsorganization_story_list'),
    path('<pk>/story/list/', story.NewsOrganizationNetworkStoryListView.as_view(), name='newsnetwork_story_list'),
    #Item
    path('story/<story>/item/add/', item.ItemPreCreateView.as_view(), name="item_precreate"),
    path('story/<story>/item/add/<pk>/', item.ItemCreateView.as_view(), name="item_add"),
    path('story/<story>/item/<pk>/update/', item.ItemUpdateView.as_view(), name="item_update"),
    path('story/<story>/item/<pk>/delete/', item.ItemDeleteView.as_view(), name="item_delete"),
    # Item templates
    path('item/templates/', item_template.ItemTemplateListView.as_view(), name="item_template_list"),
    path('item/templates/create/', item_template.ItemTemplateCreateView.as_view(), name="item_template_create"),
    path('item/templates/<pk>/', item_template.ItemTemplateDetailView.as_view(), name="item_template_detail"),
    path('item/templates/<pk>/update/', item_template.ItemTemplateUpdateView.as_view(), name="item_template_update"),
    path('item/templates/<pk>/delete/', item_template.ItemTemplateDeleteView.as_view(), name="item_template_delete"),
    # Asset
    path('library', asset.AssetLibraryTemplateView.as_view(), name='asset_library'),
    # # Image Asset
    path('images/', asset.ImageAssetLibraryTemplateView.as_view(), name='image_asset_list'),
    path('image/new/', asset.ImageAssetCreateView.as_view(), name='upload_image'),
    path('image/<pk>/', asset.ImageAssetUpdateView.as_view(), name='image_asset_detail'),
    path('image/<pk>/delete/', asset.ImageAssetDeleteView.as_view(), name='image_asset_delete'),
    path('image/<pk>/item/<item>/remove/', asset.ImageAssetDisassociateView.as_view(), name='image_asset_remove'),
    path('story/<story>/item/<item>/images/add/', asset.LibraryImageAssociateView.as_view(), name='library_image_add'),
    # # Document Asset
    path('documents/', asset.DocumentAssetLibraryTemplateView.as_view(), name='document_asset_list'),
    path('document/new/', asset.DocumentAssetCreateView.as_view(), name='upload_document'),
    path('document/<pk>/', asset.DocumentAssetUpdateView.as_view(), name='document_asset_detail'),
    path('document/<pk>/delete/', asset.DocumentAssetDeleteView.as_view(), name='document_asset_delete'),
    path('document/<pk>/item/<item>/remove/', asset.DocumentAssetDisassociateView.as_view(), name='document_asset_remove'),
    path('story/<story>/item/<item>/documents/add/', asset.LibraryDocumentAssociateView.as_view(), name='library_document_add'),
    # # Audio Asset
    path('audio/', asset.AudioAssetLibraryTemplateView.as_view(), name='audio_asset_list'),
    path('audio/new/', asset.AudioAssetCreateView.as_view(), name='upload_audio'),
    path('audio/<pk>/', asset.AudioAssetUpdateView.as_view(), name='audio_asset_detail'),
    path('audio/<pk>/delete/', asset.AudioAssetDeleteView.as_view(), name='audio_asset_delete'),
    path('audio/<pk>/item/<item>/remove/', asset.AudioAssetDisassociateView.as_view(), name='audio_asset_remove'),
    path('story/<story>/item/<item>/audio/add/', asset.LibraryAudioAssociateView.as_view(), name='library_audio_add'),
    # # Video Asset
    path('video/', asset.VideoAssetLibraryTemplateView.as_view(), name='video_asset_list'),
    path('video/new/', asset.VideoAssetCreateView.as_view(), name='upload_video'),
    path('video/<pk>/', asset.VideoAssetUpdateView.as_view(), name='video_asset_detail'),
    path('video/<pk>/delete/', asset.VideoAssetDeleteView.as_view(), name='video_asset_delete'),
    path('video/<pk>/item/<item>/remove/', asset.VideoAssetDisassociateView.as_view(), name='video_asset_remove'),
    path('story/<story>/item/<item>/video/add/', asset.LibraryVideoAssociateView.as_view(), name='library_video_add'),
    # # Simple Library
    path('internalassets/', asset.SimpleAssetLibraryTemplateView.as_view(), name='simple_asset_library'),
    path('internalassets/images/', asset.SimpleImageAssetLibraryTemplateView.as_view(), name='simple_image_asset_library'),
    path('internalassets/documents/', asset.SimpleDocumentAssetLibraryTemplateView.as_view(), name='simple_document_asset_library'),
    path('internalassets/audio/', asset.SimpleAudioAssetLibraryTemplateView.as_view(), name='simple_audio_asset_library'),
    path('internalassets/video/', asset.SimpleVideoAssetLibraryTemplateView.as_view(), name='simple_video_asset_library'),
    # # Simple Image
    path('internalassets/simpleimage/new/', asset.SimpleImageCreateView.as_view(), name='upload_simple_image'),
    path('internalassets/simpleimage/add/', asset.SimpleImageLibraryAssociateView.as_view(), name='library_simpleimage_add'),
    path('internalassets/simpleimage/<pk>/', asset.SimpleImageUpdateView.as_view(), name='simple_image_detail'),
    path('internalassets/simpleimage/<pk>/delete/', asset.SimpleImageAssetDeleteView.as_view(), name='simple_image_delete'),
    path('internalassets/simpleimage/<pk>/remove/', asset.SimpleImageAssetDisassociateView.as_view(), name='simple_image_remove'),
    # # Simple Document
    path('internalassets/simpledocument/new/', asset.SimpleDocumentCreateView.as_view(), name='upload_simple_document'),
    path('internalassets/simpledocument/add/', asset.SimpleDocumentLibraryAssociateView.as_view(), name='library_simpledocument_add'),
    path('internalassets/simpledocument/<pk>/', asset.SimpleDocumentUpdateView.as_view(), name='simple_document_detail'),
    path('internalassets/simpledocument/<pk>/delete/', asset.SimpleDocumentAssetDeleteView.as_view(), name='simple_document_delete'),
    path('internalassets/simpledocument/<pk>/remove/', asset.SimpleDocumentAssetDisassociateView.as_view(), name='simple_document_remove'),
    # # Simple Audio
    path('internalassets/simpleaudio/new/', asset.SimpleAudioCreateView.as_view(), name='upload_simple_audio'),
    path('internalassets/simpleaudio/add/', asset.SimpleAudioLibraryAssociateView.as_view(), name='library_simpleaudio_add'),
    path('internalassets/simpleaudio/<pk>/', asset.SimpleAudioUpdateView.as_view(), name='simple_audio_detail'),
    path('internalassets/simpleaudio/<pk>/delete/', asset.SimpleAudioAssetDeleteView.as_view(), name='simple_audio_delete'),
    path('internalassets/simpleaudio/<pk>/remove/', asset.SimpleAudioAssetDisassociateView.as_view(), name='simple_audio_remove'),
    # # Simple Video
    path('internalassets/simplevideo/new/', asset.SimpleVideoCreateView.as_view(), name='upload_simple_video'),
    path('internalassets/simplevideo/add/', asset.SimpleVideoLibraryAssociateView.as_view(), name='library_simplevideo_add'),
    path('internalassets/simplevideo/<pk>/', asset.SimpleVideoUpdateView.as_view(), name='simple_video_detail'),
    path('internalassets/simplevideo/<pk>/delete/', asset.SimpleVideoAssetDeleteView.as_view(), name='simple_video_delete'),
    path('internalassets/simplevideo/<pk>/remove/', asset.SimpleVideoAssetDisassociateView.as_view(), name='simple_video_remove'),

]

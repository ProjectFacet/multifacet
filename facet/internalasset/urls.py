from django.urls import path

from .views import (
    internal_asset,
    internal_audio,
    internal_document,
    internal_image,
    internal_video,
)

app_name = 'internalasset'
urlpatterns = [
    # Internal Library
    path('internalassets/', internal_asset.InternalAssetLibraryTemplateView.as_view(), name='internal_asset_library'),
    path('internalassets/images/', internal_asset.InternalImageAssetLibraryTemplateView.as_view(), name='internal_image_asset_library'),
    path('internalassets/documents/', internal_asset.InternalDocumentAssetLibraryTemplateView.as_view(), name='internal_document_asset_library'),
    path('internalassets/audio/', internal_asset.InternalAudioAssetLibraryTemplateView.as_view(), name='internal_audio_asset_library'),
    path('internalassets/video/', internal_asset.InternalVideoAssetLibraryTemplateView.as_view(), name='internal_video_asset_library'),
    # Internal Image
    path('internalassets/internalimage/new/', internal_image.InternalImageCreateView.as_view(), name='upload_internal_image'),
    path('internalassets/internalimage/add/', internal_image.InternalImageLibraryAssociateView.as_view(), name='library_internalimage_add'),
    path('internalassets/internalimage/<pk>/', internal_image.InternalImageUpdateView.as_view(), name='internal_image_detail'),
    path('internalassets/internalimage/<pk>/delete/', internal_image.InternalImageAssetDeleteView.as_view(), name='internal_image_delete'),
    path('internalassets/internalimage/<pk>/remove/', internal_image.InternalImageAssetDisassociateView.as_view(), name='internal_image_remove'),
    # Internal Document
    path('internalassets/internaldocument/new/', internal_document.InternalDocumentCreateView.as_view(), name='upload_internal_document'),
    path('internalassets/internaldocument/add/', internal_document.InternalDocumentLibraryAssociateView.as_view(), name='library_internaldocument_add'),
    path('internalassets/internaldocument/<pk>/', internal_document.InternalDocumentUpdateView.as_view(), name='internal_document_detail'),
    path('internalassets/internaldocument/<pk>/delete/', internal_document.InternalDocumentAssetDeleteView.as_view(), name='internal_document_delete'),
    path('internalassets/internaldocument/<pk>/remove/', internal_document.InternalDocumentAssetDisassociateView.as_view(), name='internal_document_remove'),
    # Internal Audio
    path('internalassets/internalaudio/new/', internal_audio.InternalAudioCreateView.as_view(), name='upload_internal_audio'),
    path('internalassets/internalaudio/add/', internal_audio.InternalAudioLibraryAssociateView.as_view(), name='library_internalaudio_add'),
    path('internalassets/internalaudio/<pk>/', internal_audio.InternalAudioUpdateView.as_view(), name='internal_audio_detail'),
    path('internalassets/internalaudio/<pk>/delete/', internal_audio.InternalAudioAssetDeleteView.as_view(), name='internal_audio_delete'),
    path('internalassets/internalaudio/<pk>/remove/', internal_audio.InternalAudioAssetDisassociateView.as_view(), name='internal_audio_remove'),
    # Internal Video
    path('internalassets/internalvideo/new/', internal_video.InternalVideoCreateView.as_view(), name='upload_internal_video'),
    path('internalassets/internalvideo/add/', internal_video.InternalVideoLibraryAssociateView.as_view(), name='library_internalvideo_add'),
    path('internalassets/internalvideo/<pk>/', internal_video.InternalVideoUpdateView.as_view(), name='internal_video_detail'),
    path('internalassets/internalvideo/<pk>/delete/', internal_video.InternalVideoAssetDeleteView.as_view(), name='internal_video_delete'),
    path('internalassets/internalvideo/<pk>/remove/', internal_video.InternalVideoAssetDisassociateView.as_view(), name='internal_video_remove'),

]

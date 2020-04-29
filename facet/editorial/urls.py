from django.urls import path

from .views import (
    project,
    story,
)

app_name = 'editorial'
urlpatterns = [
    #Project
    path('project/new/', project.ProjectCreateView.as_view(), name='project_new'),
    path('project/<pk>/', project.ProjectDetailView.as_view(), name='project_detail'),
    path('project/<pk>/update/', project.ProjectUpdateView.as_view(), name='project_edit'),
    path('project/<pk>/delete/', project.ProjectDeleteView.as_view(), name='project_delete'),

    path('project/list/', project.ProjectListView.as_view(), name='project_list'),
    path('project/<pk>/team/edit/', project.ProjectTeamUpdateView.as_view(), name='project_team_edit'),

    path('project/<pk>/stories/', project.ProjectStoryView.as_view(), name='project_stories'),
    path('project/<pk>/assets/', project.ProjectAssetView.as_view(), name='project_assets'),
    path('project/<pk>/tasks/', project.ProjectTaskView.as_view(), name='project_tasks'),
    path('project/<pk>/notes/', project.ProjectNoteView.as_view(), name='project_notes'),
    # path('/project/<pk>/note/(?P<note>\d+)/content$', notes.NoteContent.as_view(), name='note_content'),
    path('project/<pk>/calendar/', project.ProjectScheduleView.as_view(), name='project_schedule'),

    # Story
    path('story/new/', story.StoryCreateView.as_view(), name='story_new'),
    path('story/<pk>/', story.StoryDetailView.as_view(), name='story_detail'),
    path('story/<pk>/update/', story.StoryUpdateView.as_view(), name='story_edit'),
    path('story/<pk>/delete/', story.StoryDeleteView.as_view(), name='story_delete'),

    path('story/list/', story.StoryListView.as_view(), name='story_list'),
    path('story/<pk>/team/edit/', story.StoryTeamUpdateView.as_view(), name='story_team_edit'),

    path('story/<pk>/stories/', story.StoryStoryView.as_view(), name='story_stories'),
    path('story/<pk>/assets/', story.StoryAssetView.as_view(), name='story_assets'),
    path('story/<pk>/tasks/', story.StoryTaskView.as_view(), name='story_tasks'),
    path('story/<pk>/notes/', story.StoryNoteView.as_view(), name='story_notes'),
    # path('/story/<pk>/note/(?P<note>\d+)/content$', notes.NoteContent.as_view(), name='note_content'),
    path('story/<pk>/calendar/', story.StoryScheduleView.as_view(), name='story_schedule'),


]

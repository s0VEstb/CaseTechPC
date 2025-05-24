from django.urls import path

from .views import (TopicListView, SubtopicListView, LessonListView, LessonDetailView,
                     EnrollInTopicView, MarkLessonCompletedView, SubtopicListPreview)
from .views import about_us, home_view, contacts_view

app_name = 'course'

urlpatterns = [
    path('topics/', TopicListView.as_view(), name='topics'),
    path('topics/<int:topic_id>/subtopics/', SubtopicListView.as_view(), name='subtopics'),
    path('subtopics/<int:subtopic_id>/lessons/', LessonListView.as_view(), name='lessons'),
    path('lessons/<slug:slug>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('topics/<int:topic_id>/enroll/', EnrollInTopicView.as_view(), name='enroll'),
    path('lessons/<int:lesson_id>/complete/', MarkLessonCompletedView.as_view(), name='mark_complete'),
    path('topics/<int:topic_id>/preview/', SubtopicListPreview.as_view(), name='topic_preview'),

    path('about_us/', about_us, name='about_us'),
    path('contact/', contacts_view, name='contacts'),
    path('', home_view, name='home'),
]


from django.views.generic import ListView, DetailView, View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.course import Topic, Subtopic, Lesson, Enrollment, UserProgress
from django.core.paginator import Paginator


# Список всех тем
class TopicListView(LoginRequiredMixin, ListView):
    model = Topic
    template_name = 'topic/topic_list.html'
    context_object_name = 'topics'
    paginate_by = 5


# Список подтем для конкретной темы
class SubtopicListView(LoginRequiredMixin, ListView):
    model = Subtopic
    template_name = 'topic/subtopic/sub_topic_list.html'
    context_object_name = 'subtopics'
    paginate_by = 5

    def get_queryset(self):
        self.topic = get_object_or_404(Topic, pk=self.kwargs['topic_id'])
        return Subtopic.objects.filter(topic=self.topic)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = self.topic
        return context


# Список уроков для конкретной подтемы
class LessonListView(LoginRequiredMixin, ListView):
    model = Lesson
    template_name = 'topic/subtopic/lesson/lesson_list.html'
    context_object_name = 'lessons'
    paginate_by = 5

    def get_queryset(self):
        self.subtopic = get_object_or_404(Subtopic, pk=self.kwargs['subtopic_id'])
        return Lesson.objects.filter(subtopic=self.subtopic)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtopic'] = self.subtopic
        return context


# Детали конкретного урока и отображение прогресса
class LessonDetailView(LoginRequiredMixin, DetailView):
    model = Lesson
    template_name = 'topic/subtopic/lesson/lesson_detail.html'
    context_object_name = 'lesson'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем или создаём прогресс
        progress, _ = UserProgress.objects.get_or_create(
            user=self.request.user,
            lesson=self.get_object()
        )
        context['progress'] = progress
        return context


# Запись пользователя на тему
class EnrollInTopicView(LoginRequiredMixin, View):
    def post(self, request, topic_id):
        topic = get_object_or_404(Topic, id=topic_id)
        Enrollment.objects.get_or_create(user=request.user, topic=topic)
        return redirect('course:subtopics', topic_id=topic.id)


# Отметить урок как пройденный
class MarkLessonCompletedView(LoginRequiredMixin, View):
    def post(self, request, lesson_id):
        lesson = get_object_or_404(Lesson, id=lesson_id)
        progress, _ = UserProgress.objects.get_or_create(user=request.user, lesson=lesson)
        progress.completed = True
        progress.save()
        return redirect('course:lesson_detail', slug=lesson.slug)

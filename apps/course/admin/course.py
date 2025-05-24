from django.contrib import admin
from ..models.course import CustomUser, Topic, Subtopic, Lesson, Enrollment, UserProgress

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    fields = ('title', 'slug', 'order')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('order',)

class SubtopicInline(admin.StackedInline):
    model = Subtopic
    extra = 1
    fields = ('title', 'description', 'order')
    ordering = ('order',)
    inlines = [LessonInline]

    def get_inline_instances(self, request, obj=None):
        # Чтобы вложенный LessonInline работал, нужно переопределить
        # Но Django не поддерживает вложенные inline, так что LessonInline надо добавлять только в SubtopicAdmin
        return []

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)
    inlines = [SubtopicInline]

@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'order')
    ordering = ('topic', 'order')
    inlines = [LessonInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtopic', 'order')
    ordering = ('subtopic', 'order')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic', 'enrolled_at')
    list_filter = ('topic',)
    search_fields = ('user__username', 'topic__title')

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'completed', 'last_accessed')
    list_filter = ('completed',)
    search_fields = ('user__username', 'lesson__title')

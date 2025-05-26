from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import RegisterForm, AvatarUploadForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # Получаем все курсы, на которые записан пользователь
        topics = user.enrolled_topics.all()
        progress_data = {}

        for topic in topics:
            progress_data[topic.id] = topic.get_progress_for_user(user)

        # Для каждого курса ищем следующий непройденный урок
        next_lessons = {topic.id: topic.get_next_lesson_for_user(user) for topic in topics}
        context['progress_data'] = progress_data
        context['next_lessons'] = next_lessons
        # Передаём текущего пользователя в шаблон
        context['user'] = self.request.user
        context['avatar_form'] = AvatarUploadForm(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = AvatarUploadForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Аватар успешно обновлен')
        else:
            messages.error(request, 'Ошибка при загрузке аватара')
        return redirect('accounts:profile')


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:profile')

    def form_valid(self, form):
        user = form.save() # Это сработает, если form был инициализирован с request.FILES

        login(self.request, user)
        return super().form_valid(form)



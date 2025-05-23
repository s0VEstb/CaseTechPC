from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Передаём текущего пользователя в шаблон
        context['user'] = self.request.user
        return context


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save() # Это сработает, если form был инициализирован с request.FILES

        login(self.request, user)
        return super().form_valid(form)



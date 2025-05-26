from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.user.forms import CustomAuthenticationForm
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include(('apps.user.urls', 'accounts'), namespace='accounts')),
    path('accounts/login/',
         auth_views.LoginView.as_view(form_class=CustomAuthenticationForm),
         name='login'),
    # 3) Всё остальное из contrib.auth (logout, password_change и т.д.)
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('', include('apps.course.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
    url('^catalog/', include('catalog.urls')),
    url(r'^admin/', admin.site.urls),
]


# Add Django site authentication urls (for login, logout, password management)
# urlpatterns += [
#     url(r'^accounts/', include('django.contrib.auth.urls')),
# ]

#                         or

from django.contrib.auth import views

urlpatterns += [
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout'),

    url(r'^accounts/password_change/$', views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^accounts/password_change/done/$', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    url(r'^accounts/password_reset/$', views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^accounts/password_reset/done/$', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^accounts/reset/done/$', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

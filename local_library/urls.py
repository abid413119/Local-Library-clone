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
urlpatterns += [
    url(r'^accounts/', include('account.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout_then_login

admin.autodiscover()

urlpatterns = [
    url(r'^tournament/admin/', include(admin.site.urls)),
    url(r'^tournament/', include('tournament.home.urls')),
    url(r'^tournament/', include('tournament.profiles.urls')),

    # Django AllAuth
    url(r'tournament/accounts/logout/$', logout_then_login),
    url(r'tournament/accounts/', include('allauth.urls')),
]

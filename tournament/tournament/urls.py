from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout_then_login

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('tournament.home.urls')),
    url(r'^', include('tournament.profiles.urls')),

    # Django AllAuth
    url(r'^accounts/logout/$', logout_then_login),
    url(r'^accounts/', include('allauth.urls')),
]

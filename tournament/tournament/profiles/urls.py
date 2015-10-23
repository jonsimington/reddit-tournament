from django.conf.urls import patterns, url

from .views import (ProfileView, ProfileUpdateView)

urlpatterns = patterns(
    '',

    url(r'^profile/(?P<username>.+)/$',
        ProfileView.as_view(),
        name="view_profile"),

    url(r'^profile-edit/$',
        ProfileUpdateView.as_view(),
        name="update_profile"),
)

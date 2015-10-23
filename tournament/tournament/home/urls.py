from django.conf.urls import patterns, url

from views import HomePageView

urlpatterns = patterns(
    '',
    url('^$', HomePageView.as_view(), name='home'),
)

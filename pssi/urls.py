from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin

from grants.views import GreatRequestCreateView

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', TemplateView.as_view(
        template_name='index.html',
    ), name='home'),
    url(r'^pyconindia/$', TemplateView.as_view(
        template_name='pyconindia.html',
    ), name='pyconindia-static'),
    url(r'^awards/$', TemplateView.as_view(
        template_name='awards.html',
    ), name='awards-static'),

    url(r'^grants/apply/$', GreatRequestCreateView.as_view(),
        name='grants_apply'),
    url(r'^grants/apply-success/$', TemplateView.as_view(
        template_name='grants/apply_grants_success.html',
    ), name='grants_req_success'),

    url(r'^blog/', include('blogs.urls')),
    url(r'^profile/', include('accounts.urls')),
    url(r'^payment/', include('payments.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url('^markdown/', include('django_markdown.urls')),
)

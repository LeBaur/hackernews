from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hackernews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'stories.views.index', name='index'),
    url(r'^story/$', 'stories.views.story', name='story'),
    url(r'^vote/$', 'stories.views.vote', name='vote'),
)

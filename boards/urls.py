from django.conf.urls import url, include

from .views import home, board_topics, new_topic, test_for_regex

urlpatterns = [
    url(r'^$', home, name='boards.home'),
    url(r'^(?P<pk>\d+)/$', board_topics, name='boards.topics'),
    url(r'^(?P<pk>\d+)/new/$', new_topic, name='boards.new_topic'),
    url(r'^test/(?P<key_word>[-\w]+)/$', test_for_regex, name='boards.test_regex')
]

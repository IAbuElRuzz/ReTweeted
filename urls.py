from django.conf.urls.defaults import *
import os
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from reTweet.views import home_page, tweet_response, twitter_logout, test, \
    friend_unfollow, friend_follow, retweeted_of_user

urlpatterns = patterns('',
    # Example:
    url(r'^$', home_page, name='home-page'),
    url(r'tweet/$', tweet_response, name='tweet-response'),
    url(r'retweeted-of-user/$', retweeted_of_user, name='retweeted-of-user'),
    url(r'unfollow/$', friend_unfollow, name='friend_unfollow'),
    url(r'follow/$', friend_follow, name='friend_follow'),
    url(r'test/$', test, name='tweet-test'),
    url(r'logout/$', twitter_logout, name='twitter-logout'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
       {'document_root': os.path.join(os.path.dirname(__file__), "static")}),

)
